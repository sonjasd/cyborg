# Main bot file to launch bot

import asyncio
import os
import discord
from random_classes.configcheck import configcheck
from discord.ext import commands
from os import environ
from dotenv import load_dotenv

load_dotenv()

token = environ["TOKEN"]

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

async def load():
    check_if_config_exists = configcheck.check

    print("!!! LOADING COMMANDS... !!! \n")

    amount = 0

    # Look for subclasses in ./commands
    for commandos in os.listdir('./commands'):
        if commandos.endswith('.py'):
            amount += 1

    print(str(amount) + " commands found... \n")

    # Load command subclasses "cogs"
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')

    print("!!! LOOKING FOR CONFIG... !!! \n")
    check_if_config_exists()

async def main():
    await load()
    print('!!! INITIALIZATION SUCCESS, STARTING BOT. !!! \n')
    await bot.start(token)

asyncio.run(main())