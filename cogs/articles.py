import discord
from discord import app_commands
from discord.ext import commands
import random
from utils.news_api import fetch_articles

class Articles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="article", description="Get a random or topic-specific IT article")
    async def article(self, interaction: discord.Interaction, topic: str = None):
        articles = fetch_articles(topic)
        if not articles:
            await interaction.response.send_message(f"No articles found on the topic '{topic}'. Try another topic.")
            return

        article = random.choice(articles)

        embed = discord.Embed(
            title=article["title"],
            url=article["url"],
            description=article.get("description", "No description available."),
            color=discord.Color.blue()
        )
        embed.set_footer(text=f"Source: {article.get('source', {}).get('name', 'Unknown')}")

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="Read More", url=article["url"], style=discord.ButtonStyle.link))
        view.add_item(discord.ui.Button(label="New Article", custom_id="new_article", style=discord.ButtonStyle.primary))

        await interaction.response.send_message(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(Articles(bot))
