import config
from discord.ext import commands
import discord

# This will be not specific commands.
#   -Updating status
#   -Checking latency
#   -reporting any api issues in future

class BotController(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.has_role("Officer")
    @commands.command(name="update", help ="Update Bot Playing")
    async def update_playing(self,ctx):
        activity = discord.Game(name=str(ctx.message.content).split(" ",1)[1],type = 2)
        await self.bot.change_presence(status=discord.Status.idle, activity=activity)

    @commands.command(name="status", help ="Check the bot status")
    async def get_status(self,ctx):
        await ctx.send(str(round(self.bot.latency * 1000 )) + "ms")

def setup(bot):
    bot.add_cog(BotController(bot))