"""defines commands for the qoutes functionality"""
from discord.ext import commands
from discord import app_commands
import discord
from utils.quotes import get_quote


class Quotes(commands.Cog):
    """A class for qoutes commands"""
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='quote', description='Get an inspiring quote')
    async def quote_command(self, interaction: discord.interactions):
        quote: str = get_quote()
        await self.send_quote(interaction, quote)

    async def send_quote(self, interaction, content):
        """
        """
        new_quote_button = discord.ui.Button(label="New Quote",
                                             style=discord.ButtonStyle.blurple)

        async def new_quote_callback(interaction: discord.Interaction):
            new_quote = get_quote()
            await self.send_quote(interaction, new_quote)

        new_quote_button.callback = new_quote_callback
        view = discord.ui.View()
        view.add_item(new_quote_button)
        await interaction.response.send_message(content, view=view)


async def setup(bot):
    await bot.add_cog(Quotes(bot))
