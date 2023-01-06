import os
import time
from random_classes.ch4nce import ch4nce
from random_classes.coginit import coginit as coginit
from discord.ext import commands

script = str(os.path.basename(__file__))

class flipacoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
         coginit.report(filename=script)
    
    @commands.command()
    async def flipacoin(self, ctx):
        result = ch4nce.flip()
        await ctx.send("https://tenor.com/view/coin-flip-flip-coin-gif-19747326")
        time.sleep(1)
        if result:
            await ctx.send("Heads")
        elif not result:
            await ctx.send("Tails")

async def setup(bot):
    await bot.add_cog(flipacoin(bot))
