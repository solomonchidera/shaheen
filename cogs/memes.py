"""defines commands for the memes functionality"""
from discord.ext import commands
from discord import app_commands
import discord
from utils.meme_api import get_meme


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
        await interaction.response.send_message(meme_link)


async def setup(bot):
    """ loads the memes Cog into the bot.

    Args:
        bot (command.Bot): instance of the bot.
    """
    await bot.add_cog(Memes(bot))
