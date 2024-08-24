import discord
from discord.ext import commands
import random
import json
from discord import app_commands


class Games(commands.Cog):
    """
        Games is a discord bot cog for playing some games.
    """
    def __init__(self, bot):
        """initialization fucntion

        Args:
            bot (commands.Bot): intance of the bot running the Cog.
        """
        self.bot = bot

        # Load Truth or Dare data
        with open('data/truth_or_dare.json', 'r') as f:
            data = json.load(f)
            self.truths = data["truths"]
            self.dares = data["dares"]

        # Load Never Have I Ever data
        with open('data/never_have_i_ever.json', 'r') as f:
            self.never_have_i_ever = json.load(f)["questions"]

        # Load Would You Rather data
        with open('data/would_you_rather.json', 'r') as f:
            self.would_you_rather = json.load(f)["questions"]

    def get_random_truth(self):
        return random.choice(self.truths)

    def get_random_dare(self):
        return random.choice(self.dares)

    def get_random_choice(self):
        return random.choice(["truth", "dare"])

    def get_random_never_have_i_ever(self):
        return random.choice(self.never_have_i_ever)

    def get_random_would_you_rather(self):
        return random.choice(self.would_you_rather)

    @app_commands.command(name="truth", description="Get a truth question.")
    async def truth(self, interaction: discord.Interaction):
        """
            Truth command for getting a truth question for (truth/dare) game.

            Args:
                interaction (discord.Interaction): a discord interaction.
        """
        truth_question = self.get_random_truth()
        await self.send_truth_or_dare(interaction, truth_question, is_truth=True)

    @app_commands.command(name="dare", description="Get a dare challenge.")
    async def dare(self, interaction: discord.Interaction):
        """
            Dare command for getting a dare for (truth/dare) game.

            Args:
                interaction (discord.Interaction): a discord interaction.
        """
        dare_challenge = self.get_random_dare()
        await self.send_truth_or_dare(interaction, dare_challenge, is_truth=False)

    async def send_truth_or_dare(self, interaction, content, is_truth):
        truth_button = discord.ui.Button(label="Truth", style=discord.ButtonStyle.primary)
        dare_button = discord.ui.Button(label="Dare", style=discord.ButtonStyle.danger)
        random_button = discord.ui.Button(label="Random", style=discord.ButtonStyle.success)

        async def truth_callback(interaction: discord.Interaction):
            new_truth = self.get_random_truth()
            await self.send_truth_or_dare(interaction, new_truth, is_truth=True)

        async def dare_callback(interaction: discord.Interaction):
            new_dare = self.get_random_dare()
            await self.send_truth_or_dare(interaction, new_dare, is_truth=False)

        async def random_callback(interaction: discord.Interaction):
            if self.get_random_choice() == "truth":
                new_truth = self.get_random_truth()
                await self.send_truth_or_dare(interaction, new_truth, is_truth=True)
            else:
                new_dare = self.get_random_dare()
                await self.send_truth_or_dare(interaction, new_dare, is_truth=False)

        truth_button.callback = truth_callback
        dare_button.callback = dare_callback
        random_button.callback = random_callback

        view = discord.ui.View()
        view.add_item(truth_button)
        view.add_item(dare_button)
        view.add_item(random_button)

        await interaction.response.send_message(content, view=view)

    @app_commands.command(name="neverhaveiever", description="Get a 'Never Have I Ever' question.")
    async def never_have_i_ever(self, interaction: discord.Interaction):
        """
            Never have I ever command for never Have I ever Game.

            Args:
                interaction (discord.Interaction): a discord interaction.
        """
        question = self.get_random_never_have_i_ever()
        await self.send_never_have_i_ever(interaction, question)

    async def send_never_have_i_ever(self, interaction, content):
        yes_button = discord.ui.Button(label="Yes", style=discord.ButtonStyle.primary)
        no_button = discord.ui.Button(label="No", style=discord.ButtonStyle.danger)
        new_question_button = discord.ui.Button(label="New Question", style=discord.ButtonStyle.success)

        async def yes_callback(interaction: discord.Interaction):
            await interaction.response.send_message("You answered: Yes!")

        async def no_callback(interaction: discord.Interaction):
            await interaction.response.send_message("You answered: No!")

        async def new_question_callback(interaction: discord.Interaction):
            new_question = self.get_random_never_have_i_ever()
            await self.send_never_have_i_ever(interaction, new_question)

        yes_button.callback = yes_callback
        no_button.callback = no_callback
        new_question_button.callback = new_question_callback

        view = discord.ui.View()
        view.add_item(yes_button)
        view.add_item(no_button)
        view.add_item(new_question_button)

        await interaction.response.send_message(content, view=view)

    @app_commands.command(name="wouldyourather", description="Get a 'Would You Rather' question.")
    async def would_you_rather(self, interaction: discord.Interaction):
        """
            would you rather command for would you rather Game.

            Args:
                interaction (discord.Interaction): a discord interaction.
        """
        question = self.get_random_would_you_rather()
        await self.send_would_you_rather(interaction, question)

    async def send_would_you_rather(self, interaction, content):
        option_1_button = discord.ui.Button(label="Option 1", style=discord.ButtonStyle.primary)
        option_2_button = discord.ui.Button(label="Option 2", style=discord.ButtonStyle.primary)
        new_question_button = discord.ui.Button(label="New Question", style=discord.ButtonStyle.success)

        async def option_1_callback(interaction: discord.Interaction):
            await interaction.response.send_message(f"{interaction.user} voted for: Option 1!")

        async def option_2_callback(interaction: discord.Interaction):
            await interaction.response.send_message(f"{interaction.user} voted for: Option 2!")

        async def new_question_callback(interaction: discord.Interaction):
            new_question = self.get_random_would_you_rather()
            await self.send_would_you_rather(interaction, new_question)

        option_1_button.callback = option_1_callback
        option_2_button.callback = option_2_callback
        new_question_button.callback = new_question_callback

        view = discord.ui.View()
        view.add_item(option_1_button)
        view.add_item(option_2_button)
        view.add_item(new_question_button)

        await interaction.response.send_message(content, view=view)


async def setup(bot: commands.Bot):
    """ loads the challange Cog into the bot.

    Args:
        bot (command.Bot): instance of the bot.
    """
    await bot.add_cog(Games(bot))
