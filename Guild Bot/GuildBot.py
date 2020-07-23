#Discord Guild Bot
#Store TOKENS in secrets
import secrets

import discord
from discord.ext import commands

import os

#Select a prefix for us to use. Change it to ! when the other bot is removed.
client = commands.Bot(command_prefix = ">")

#For testing. Can remove later.
@client.event
async def on_ready():
    print('Connected.')

extensions = ['cogs.GeneralCommands', 'cogs.SuggestionCommands']

if __name__ == '__main__':
    for item in extensions:
        client.load_extension(item)

client.run(secrets.DISCORD_TOKEN)
