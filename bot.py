import asyncio
import os
import discord
from discord.ext import commands
from os import environ
from dotenv import load_dotenv

load_dotenv()

token = environ["TOKEN"]

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

async def load():
    print("!!! LOADING COMMANDS... !!! \n")

    amount = 0

    for commandos in os.listdir('./commands'):
        if commandos.endswith('.py'):
            amount += 1

    print(str(amount) + " commands found... \n")

    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')

async def main():
    await load()
    await bot.start(token)

asyncio.run(main())