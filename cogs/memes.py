"""defines commands for the memes functionality"""
from discord.ext import commands
from discord import app_commands
import discord
from utils.meme_api import get_meme
import os


class Memes(commands.Cog):
    """
    """
    def __init__(self, bot):
        """initalization function"""
        self.bot = bot

    @app_commands.command(name='meme',
                          description='A meme to light up your day')
    async def meme_command(self, interaction: discord.Interaction):
        """
        """
        meme_link = get_meme()
        await self.send_meme(interaction, meme_link)

    async def send_meme(self, interaction: discord.Interaction, content: str) -> None:
        """
        """
        new_meme_button = discord.ui.button(label='New Meme😜',
                                            style=discord.ButtonStyle.primary)
        async def new_meme_callback(interaction: discord.Interaction):
            """_summary_
            """
            new_meme = get_meme()
            await self.send_meme(interaction, new_meme)

        new_meme_button.callback = new_meme_callback

        view = discord.ui.View()
        view.add_item(new_meme_button)
        view.add_item(discord.ui.Button(label="Invite", url=os.getenv('INVITE_LINK'), style=discord.ButtonStyle.link))

        await interaction.response.send_message(content, view=view)

async def setup(bot):
    """ loads the memes Cog into the bot.

    Args:
        bot (command.Bot): instance of the bot.
    """
    await bot.add_cog(Memes(bot))
