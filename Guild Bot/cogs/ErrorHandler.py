import config
from discord.ext import commands
import discord

# Handle all errors here. There shouldn't be a need for custom ones as we can just refer people back to the >help


class ErrorHandler(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send('Required Arguments Missing.')
        if isinstance(error,commands.CommandNotFound):
            await ctx.send('Command Not Found. Please use >help for list of commands.')

def setup(bot):
    bot.add_cog(ErrorHandler(bot))