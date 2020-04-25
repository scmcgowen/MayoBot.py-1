import discord
from discord.ext import commands


class Katze(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def warn(self, ctx, user, reasons):
if ctx.message.author.id == 474364264644083712:
       reason  = ""
        for reason_part in msgs:
            reason = reason + reason_part + " "

        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send(user" has been warned for "reason)

def setup(bot):
    bot.add_cog(Say(bot))
