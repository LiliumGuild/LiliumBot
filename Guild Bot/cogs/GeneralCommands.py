import config
from discord.ext import commands

##These will be general commands for users to type. Simple input -> output. Games we play, contacting an officer, etc

class GeneralCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

        self.OFFICER_CHANNEL = config.OFFICER_CHANNEL
    
    @commands.command(name="officer", help ="A command to contact Officers")
    async def contact_officer(self,ctx):
        officer_channel = self.bot.get_channel(675650987100209152)
        await officer_channel.send(str(ctx.author.name) + " posted the following message for Officers: " + str(ctx.message.content).split(" ",1)[1])

        await ctx.channel.send(ctx.author.name + ", Your message has been sent to the Officers.")
        await ctx.message.delete()
        
    @commands.command(name = "praise", help = "Use this command if you like the bot")
    async def command_praise(self,ctx):
        await ctx.channel.send("If you found this bot helpful, Message Neferra and tell her what a good boy Stretch is. \nIngame: Neferra \nDiscord: Adenel#4329")

def setup(bot):
    bot.add_cog(GeneralCommands(bot))