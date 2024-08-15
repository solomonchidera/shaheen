from discord.ext import commands
from discord import app_commands
import discord


class Readme(commands.Cog):
    """ Class for the Readme command """

    def __init__(self, bot):
        """initialization function
        """
        self.bot = bot

        with open('data/readme_template1.md', 'r') as f:
            self.temp1 = f.read()

        # Load Would You Rather data
        with open('data/readme_template2.md', 'r') as f:
            self.temp2 = f.read()

    @app_commands.command(name='readme',
                          description='templates for creating a readme file')
    async def readme_command(self, interaction: discord.Interaction):
        """ a command for getting a readme file template.

        Args:
            interaction (discord.Interaction): object for interactiong
            with commands.
        """
        temp1_button = discord.ui.Button(label="📑Template 1",
                                         style=discord.ButtonStyle.primary)
        temp2_button = discord.ui.Button(label="📑Template 2",
                                         style=discord.ButtonStyle.primary)

        async def temp1_callback(interaction: discord.Interaction):
            await interaction.response.send_message(f"```{self.temp1}```")

        async def temp2_callback(interaction: discord.Interaction):
            await interaction.response.send_message(f"```{self.temp2}```")

        temp1_button.callback = temp1_callback
        temp2_button.callback = temp2_callback

        view = discord.ui.View()
        view.add_item(temp1_button)
        view.add_item(temp2_button)

        await interaction.response.send_message(content="Choose template",
                                                view=view)


async def setup(bot):
    """ loads the quote Cog into the bot.

    Args:
        bot (command.Bot): instance of the bot.
    """
    await bot.add_cog(Readme(bot))
