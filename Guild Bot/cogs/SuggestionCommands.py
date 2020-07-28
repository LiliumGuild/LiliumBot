import config
from discord.ext import commands
import discord

class SuggestionCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
        self.EVENT_CHANNEL = config.EVENT_CHANNEL
        self.MEDIA_CHANNEL = config.MEDIA_CHANNEL
        self.GRAPHIC_CHANNEL = config.GRAPHIC_CHANNEL
        self.RAID_CHANNEL = config.RAID_CHANNEL
        self.RECRUITMENT_CHANNEL = config.RECRUITMENT_CHANNEL

    @commands.command(name="suggestevent", help ="Suggest a guild event!")
    async def command_suggest_event(self,ctx):
        await self.bot.get_channel(self.EVENT_CHANNEL).send(str(ctx.author.name) + " posted the following message for Event-Related: " + str(ctx.message.content).split(" ",1)[1])
        await ctx.channel.send(ctx.author.name + ", Your message has been sent to the Event Team.")
        await ctx.message.delete()
    
    @commands.command(name="suggestmedia", help ="Suggest media the guild could make!")
    async def command_suggest_media(self,ctx):
        await self.bot.get_channel(self.MEDIA_CHANNEL).send(str(ctx.author.name) + " posted the following message for Media-Related: " + str(ctx.message.content).split(" ",1)[1])
        await ctx.channel.send(ctx.author.name + ", Your message has been sent to the Media Team.")
        await ctx.message.delete()

    @commands.command(name="suggestgraphic", help ="Suggest a graphic for the guild!")
    async def command_suggest_graphic(self,ctx):
        await self.bot.get_channel(self.GRAPHIC_CHANNEL).send(str(ctx.author.name) + " posted the following message for Graphic-Related: " + str(ctx.message.content).split(" ",1)[1])
        await ctx.channel.send(ctx.author.name + ", Your message has been sent to the Graphic Team.")
        await ctx.message.delete()
    
    @commands.command(name="suggestraid", help ="Suggest a raid the guild could do!")
    async def command_suggest_raid(self,ctx):
        await self.bot.get_channel(self.RAID_CHANNEL).send(str(ctx.author.name) + " posted the following message for Raid-Related: " + str(ctx.message.content).split(" ",1)[1])
        await ctx.channel.send(ctx.author.name + ", Your message has been sent to the Raid Team.")
        await ctx.message.delete()

    @commands.command(name="suggestrecruit", help ="Suggest a way we can recruit more members!")
    async def command_suggest_recruit(self,ctx):
        await self.bot.get_channel(self.RECRUITMENT_CHANNEL).send(str(ctx.author.name) + " posted the following message for Recruitment-Related: " + str(ctx.message.content).split(" ",1)[1])
        #await ctx.channel.send(ctx.author.name + ", Your message has been sent to the Recruitment Team.")
        await ctx.channel.send(embed=suggestionClarify("Recruitment",ctx.author.name))
        await ctx.message.delete()

def suggestionClarify(section, author):

    embed = discord.Embed(colour = discord.Colour.from_rgb(32, 77, 26), title = section + " Suggestion")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/734891304651194418/650c1722bfef6a6dacd1216b7a440a3a.png")
    embed.add_field(name = author + ", Your message has been sent to the " +  section + " Team!", value = "Thank you for your suggestion.")
    return embed

def setup(bot):
    bot.add_cog(SuggestionCommands(bot))