import discord
from discord import app_commands
from discord.ext import commands
import google.generativeai as genai
import os

# Your Google API key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

class Projects(commands.Cog):
    """ Projects Cog that provides a /project command to generate project ideas. """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.previous_ideas = set()  # Set to store previously suggested ideas
        self.model = genai.GenerativeModel('gemini-pro')

    @app_commands.command(name="project", description="Suggest a new project idea for the day, week, or month.")
    async def project(self, interaction: discord.Interaction) -> None:
        """
        Project command that fetches a project idea from Google Gemini API and presents it to the user.
        """
        # Acknowledge interaction early with a loading message
        await interaction.response.defer()

        # Fetch project idea and estimated duration
        project_idea, estimated_duration = await self.fetch_project_idea()

        # Create an embed to display the project idea and estimated duration
        embed = discord.Embed(
            title="🚀 New Project Idea",
            description=project_idea,
            color=discord.Color.blue()
        )
        embed.add_field(name="Estimated Duration", value=estimated_duration)

        # Create a view (which includes the button)
        view = ProjectView(self.fetch_project_idea)  # Pass the fetch_project_idea function

        # Update the original deferred response with the final content
        await interaction.followup.send(embed=embed, view=view)

    async def fetch_project_idea(self):
        """
        Fetch a project idea and its estimated duration using Google Gemini API.
        """
        try:
            prompt = "Generate a unique coding project idea and an estimated completion time. Format the response as 'Project Idea: [idea]\nEstimated Duration: [duration]'"
            response = await self.model.generate_content_async(prompt)

            # Extract the idea and duration from the response
            content = response.text.strip().split('\n')
            project_idea = content[0].replace('Project Idea: ', '')
            estimated_duration = content[1].replace('Estimated Duration: ', '')

            # Check if the idea was already suggested before
            if project_idea in self.previous_ideas:
                return await self.fetch_project_idea()  # Recursively get a new idea if it's already been suggested

            self.previous_ideas.add(project_idea)  # Add the idea to the set of previous suggestions

            return project_idea, estimated_duration

        except Exception as e:
            # Handle any errors while fetching project idea
            print(f"Error fetching project idea: {e}")
            return "Sorry, I couldn't fetch a project idea. Please try again later.", "Unknown"


# Button logic for fetching a new project idea
class NewProjectButton(discord.ui.Button):
    def __init__(self, fetch_project_idea):
        super().__init__(label="New Idea", style=discord.ButtonStyle.primary, custom_id="new_project")
        self.fetch_project_idea = fetch_project_idea

    async def callback(self, interaction: discord.Interaction):
        # Fetch a new project idea using the function passed during initialization
        project_idea, estimated_duration = await self.fetch_project_idea()
        embed = discord.Embed(
            title="🚀 New Project Idea",
            description=project_idea,
            color=discord.Color.blue()
        )
        embed.add_field(name="Estimated Duration", value=estimated_duration)

        # Edit the message with the new project idea
        await interaction.response.edit_message(embed=embed)


# View that includes the button
class ProjectView(discord.ui.View):
    def __init__(self, fetch_project_idea):
        super().__init__()
        self.add_item(NewProjectButton(fetch_project_idea))
        self.add_item(discord.ui.Button(
            label="Invite",
            url=os.getenv('INVITE_LINK'),
            style=discord.ButtonStyle.link
        ))



# Cog setup function
async def setup(bot: commands.Bot) -> None:
    """ Loads the Projects Cog into the bot. """
    await bot.add_cog(Projects(bot))
