#!/bin/bash

# Create subdirectories
mkdir -p cogs
mkdir -p data
mkdir -p utils

# Create main files
touch bot.py
touch config.py
touch requirements.txt

# Create cog files
touch cogs/__init__.py
touch cogs/games.py
touch cogs/youtube.py
touch cogs/projects.py
touch cogs/challenges.py
touch cogs/quotes.py
touch cogs/memes.py
touvh cogs/articles.py

# Create data files
touch data/preferences.db
touch data/never_have_i_ever.json
touch data/truth_or_dare.json
touch data/would_you_rather.json
touch data/responses.json

# Create utility files
touch utils/__init__.py
touch utils/youtube_api.py

# completion message
echo "Project structure for 'shaheen' created successfully."
