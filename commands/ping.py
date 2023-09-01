import discord
from datetime import datetime
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)

        await ctx.reply(f"My latency is {latency}!")


async def setup(bot):
    await bot.add_cog(Ping(bot))