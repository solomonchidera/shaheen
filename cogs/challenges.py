import discord
from discord import app_commands
from discord.ext import commands
import requests
import random

LEETCODE_API_URL = "https://leetcode.com/graphql"

class Challenges(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="leetcode", description="Fetch a random coding challenge from LeetCode")
    async def leetcode(self, interaction: discord.Interaction, difficulty: str = None):
        # GraphQL query to fetch problems
        query = """
        query getProblems($categorySlug: String, $filters: QuestionListFilterInput) {
            problemsetQuestionList: problemsetQuestionList(
                categorySlug: $categorySlug
                filters: $filters
            ) {
                questions: data {
                    questionTitle
                    titleSlug
                    difficulty
                }
            }
        }
        """
        
        # Define the filters based on difficulty
        variables = {
            "categorySlug": "",
            "filters": {}
        }
        if difficulty:
            variables["filters"]["difficulty"] = difficulty.upper()

        response = requests.post(LEETCODE_API_URL, json={"query": query, "variables": variables})
        data = response.json()

        if response.status_code == 200 and "data" in data:
            questions = data["data"]["problemsetQuestionList"]["questions"]

            if not questions:
                await interaction.response.send_message(f"No challenges found for difficulty: {difficulty}")
                return

            # Select a random challenge
            challenge = random.choice(questions)

            embed = discord.Embed(
                title=challenge["questionTitle"],
                url=f"https://leetcode.com/problems/{challenge['titleSlug']}/",
                description=f"Difficulty: {challenge['difficulty']}",
                color=discord.Color.green()
            )

            # Add a button to fetch a new challenge
            view = discord.ui.View()
            view.add_item(discord.ui.Button(label="Try this challenge", url=f"https://leetcode.com/problems/{challenge['titleSlug']}/", style=discord.ButtonStyle.link))
            view.add_item(discord.ui.Button(label="New Challenge", custom_id="new_challenge", style=discord.ButtonStyle.primary))

            await interaction.response.send_message(embed=embed, view=view)

        else:
            await interaction.response.send_message("Failed to fetch challenges from LeetCode. Please try again later.")

async def setup(bot):
    await bot.add_cog(Challenges(bot))