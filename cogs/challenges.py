import discord
from discord import app_commands
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random
import time

LEETCODE_URL = "https://leetcode.com/problemset/all/"

class Challenges(commands.Cog):
    """Challenges is a Discord bot Cog for fetching coding challenges from LeetCode."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="leetcode", description="Fetch a random coding challenge from LeetCode")
    async def leetcode(self, interaction: discord.Interaction) -> None:
        """
        Fetches a random coding challenge from LeetCode using web scraping.
        """

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }

        # Send the GET request to LeetCode
        response = requests.get(LEETCODE_URL, headers=headers)

        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all problem links
            problems = soup.find_all('a', class_='title-cell__ZGos')

            # Check if problems were found
            if not problems:
                await interaction.response.send_message("No problems found. Please try again later.")
                return

            # Select a random problem
            problem = random.choice(problems)

            title = problem.text.strip()
            link = "https://leetcode.com" + problem['href']
            difficulty = "Unknown"  # Placeholder as difficulty may not be available directly

            # Create an embed message
            embed = discord.Embed(
                title=title,
                url=link,
                description=f"Difficulty: {difficulty}",
                color=discord.Color.green()
            )

            # Add a button to fetch a new challenge
            view = discord.ui.View()
            view.add_item(discord.ui.Button(label="Try this challenge", url=link, style=discord.ButtonStyle.link))
            view.add_item(discord.ui.Button(label="New Challenge", custom_id="new_challenge", style=discord.ButtonStyle.primary))

            await interaction.response.send_message(embed=embed, view=view)

        else:
            await interaction.response.send_message("Failed to fetch challenges from LeetCode. Please try again later.")

async def setup(bot: commands.Bot) -> None:
    """
    Loads the Challenges Cog into the bot.
    """
    await bot.add_cog(Challenges(bot))