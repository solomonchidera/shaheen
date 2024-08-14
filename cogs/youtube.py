import os
import discord
from discord import app_commands
from discord.ext import commands
import random
from utils.youtube_api import fetch_random_video

class YouTube(commands.Cog):
    """
    YouTube is a Discord bot Cog for fetching and sending YouTube videos.
    """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="youtube", description="Fetch and send a random tech YouTube video or search by topic")
    async def youtube(self, interaction: discord.Interaction, topic: str = None) -> None:
        """
        Fetches YouTube videos. If no topic is provided, fetches a random tech video.
        """
        try:
            if not topic:
                topic = "technology"

            videos = fetch_random_video(topic)
            if not videos:
                await interaction.response.send_message(f"No videos found for topic: {topic}")
                return

            video = random.choice(videos)
            video_title = video['snippet']['title']
            video_url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"

            embed = discord.Embed(
                title=video_title,
                url=video_url,
                description=f"Topic: {topic}",
                color=discord.Color.red()
            )
            embed.set_thumbnail(url=video['snippet']['thumbnails']['high']['url'])

            view = discord.ui.View()
            view.add_item(discord.ui.Button(label="Watch Now", url=video_url, style=discord.ButtonStyle.link))
            view.add_item(discord.ui.Button(label="Invite", url=os.getenv('INVITE_LINK'), style=discord.ButtonStyle.link))

            await interaction.response.send_message(embed=embed, view=view)

        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {str(e)}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(YouTube(bot))