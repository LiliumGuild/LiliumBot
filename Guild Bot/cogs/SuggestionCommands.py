from discord.ext import commands

class SuggestionCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name="suggestevent", help ="Suggest a guild event!")
    async def command_suggest_event(self,ctx):
        await self.bot.get_channel(734734639230615581).send(str(ctx.author.name) + " posted the following message for Event-Related: " + str(ctx.message.content).split(" ",1)[1])
        await ctx.channel.send(ctx.author.name + ", Your message has been sent to the Event Team.")
        await ctx.message.delete()
    
    @commands.command(name="suggestmedia", help ="Suggest media the guild could make!")
    async def command_suggest_media(self,ctx):
        await self.bot.get_channel(734734538160472176).send(str(ctx.author.name) + " posted the following message for Media-Related: " + str(ctx.message.content).split(" ",1)[1])
        await ctx.channel.send(ctx.author.name + ", Your message has been sent to the Media Team.")
        await ctx.message.delete()

    @commands.command(name="suggestgraphic", help ="Suggest a graphic for the guild!")
    async def command_suggest_graphic(self,ctx):
        await self.bot.get_channel(734741278012735520).send(str(ctx.author.name) + " posted the following message for Graphic-Related: " + str(ctx.message.content).split(" ",1)[1])
        await ctx.channel.send(ctx.author.name + ", Your message has been sent to the Graphic Team.")
        await ctx.message.delete()
    
    @commands.command(name="suggestraid", help ="Suggest a raid the guild could do!")
    async def command_suggest_raid(self,ctx):
        await self.bot.get_channel(734744054956294154).send(str(ctx.author.name) + " posted the following message for Raid-Related: " + str(ctx.message.content).split(" ",1)[1])
        await ctx.channel.send(ctx.author.name + ", Your message has been sent to the Raid Team.")
        await ctx.message.delete()

    @commands.command(name="suggestrecruit", help ="Suggest a way we can recruit more members!")
    async def command_suggest_recruit(self,ctx):
        await self.bot.get_channel(732123646759403531).send(str(ctx.author.name) + " posted the following message for Recruitment-Related: " + str(ctx.message.content).split(" ",1)[1])
        await ctx.channel.send(ctx.author.name + ", Your message has been sent to the Recruitment Team.")
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(SuggestionCommands(bot))