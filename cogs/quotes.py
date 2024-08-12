"""defines commands for the qoutes functionality"""
from discord.ext import commands
import discord
from utils.quotes import get_quote


class Quotes(commands.Cog):
    """A class for qoutes commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Quote')
    async def quote_command(self, ctx):
        quote: str = get_quote()
        await ctx.send(quote)


async def setup(bot):
    await bot.add_cog(Quotes(bot))
