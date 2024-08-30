"""
Main Entry point for shaheen bot that loads the cogs 
and boot the bot
"""
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

activities = [
    discord.Game(name="MW3", platform="PS5")
#    discord.Game(name="FIFA 23", platform="XBOX")
#    discord.Game(name="Warzone")
#    discord.Watching(name="The Crow")
#    discord.Watching(name="Over the server")
#    discord.Listening(name="Lofi Beats")
#    discord.Listening(name="The Nights")
        ]

# Load cogs
async def load_cogs():
    await bot.load_extension('cogs.games')
    await bot.load_extension('cogs.about')
    await bot.load_extension('cogs.youtube')
    await bot.load_extension('cogs.quotes')
    await bot.load_extension('cogs.articles')
    await bot.load_extension('cogs.projects')
    await bot.load_extension('cogs.memes')
    await bot.load_extension('cogs.readme')
#    await bot.load_extension('cogs.challenges')

# Shuffle events here
@tasks.loop(minutes=30) # 30minutes
async def change_activity():
    current_activity = random.choice(activities)
    await bot.change_presence(status=discord.Status.dnd, activity=current_activity)
    print(f"Bot statues updated to: {current_activity.name} ({current_activity.type.name})")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id}).')
    await load_cogs()

    # custom status
    """
    Below script could be twicked to the prefered state of the bot which could be
    dnd
    idle
    invisible
    online which is default without the line
    """
    change_activity.start() # call change activity function

    # custom script end
    await bot.tree.sync()
    print(f"slash commands synced and registered for {bot.user}.")

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
