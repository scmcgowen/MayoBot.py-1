import discord
from discord.ext import commands


class SayCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *msgs):

        msg = ""
        for msg_part in msgs:
            msg = msg + msg_part + " "

        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send(msg)
