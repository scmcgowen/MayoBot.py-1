import discord
from discord.ext import commands


class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send("🚫| Oh no! An error has occurred:\n`%s`" % str(error))
      

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))