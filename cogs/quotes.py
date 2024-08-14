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
        """ Defines "quote" command that gives a qoute to the user.

        Args:
            interaction (discord.interactions): object for interacting with
            commands.
        """

        quote: str = get_quote()
        await self.send_quote(interaction, quote)

    async def send_quote(self, interaction: discord.Interaction, content: str):
        """ prepare the command response and send it as a response
            also defines a button and a callback for the command
        Args:
            interaction (discord.interaction): command interaction object.
            content (str): content returned by the command
        """
        new_quote_button = discord.ui.Button(label="New Quote",
                                             style=discord.ButtonStyle.blurple)

        async def new_quote_callback(interaction: discord.Interaction):
            """ Nested recursive function to handle button callback

            Args:
                interaction (discord.Interaction): command interaction object
            """
            new_quote = get_quote()
            await self.send_quote(interaction, new_quote)

        # assign the callback function to the button
        new_quote_button.callback = new_quote_callback

        # creating a view and adding the button to the view
        view = discord.ui.View()
        view.add_item(new_quote_button)

        # sending a resonse
        await interaction.response.send_message(content, view=view)


async def setup(bot):
    """ loads the quote Cog into the bot.

    Args:
        bot (command.Bot): instance of the bot.
    """
    await bot.add_cog(Quotes(bot))
