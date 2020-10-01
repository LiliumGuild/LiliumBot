#Discord Guild Bot
#Store TOKENS in secrets
import secrets
import os

import discord
from discord.ext import commands

#Select a prefix for us to use. Change it to ! when the other bot is removed.
client = commands.Bot(command_prefix = ">")

#For testing. Can remove later.
@client.event
async def on_ready():
    print('Connected.')
    
# Load all cogs in the cogs folder
if __name__ == '__main__':
    for filename in os.listdir('./Guild Bot/cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

client.run(secrets.DISCORD_TOKEN)

