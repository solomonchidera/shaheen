import discord
from discord import app_commands
from discord.ext import commands
import os

class About(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="about", description="Display information about shaheen bot")
    async def about(self, interaction: discord.Interaction):
        # Embed with bot information
        embed = discord.Embed(
            title="About Shaheen Bot",
            description="I'm a bot that offer games for developers and other cools stuff to stay productive!",
            color=discord.Color.blue()
        )
        embed.add_field(name="Version", value="0.0.1", inline=True)
        embed.add_field(name="Creators", value="so1omon & y4h14", inline=True)
        embed.add_field(name="Library", value="discord.py", inline=True)
        embed.add_field(name="Commands", value="/about, /article, /dare, /neverhaveiever, /project, /quote, /truth, /wouldyourather, /youtube", inline=False)
        embed.add_field(name="Description", value="Use /project to get a new project idea with estimated duration. "
                                                  "This bot uses Google's Gemini AI to generate creative project ideas."
                                                  "Use /about to get a quick guide and description for shaheen bot"
                                                  "Use /article to get a random tech article from internet with an optional 'topic' to get a specific result"
                                                  "Use /dare to get a random developer dares", inline=False)

        # Create a view with buttons
        view = AboutView()

        await interaction.response.send_message(embed=embed, view=view)

class AboutView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Add buttons
        self.add_item(discord.ui.Button(label="Privacy Policy", style=discord.ButtonStyle.link, url='https://shaheen-toc.web.app/'))
        self.add_item(discord.ui.Button(label="Invite", style=discord.ButtonStyle.link, url=os.getenv('INVITE_LINK')))

async def setup(bot: commands.Bot):
    await bot.add_cog(About(bot))
