import discord

from discord.ext import commands


class Dad(commands.Cog):
  
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("I'm") or message.content.startswith("i'm"):
            await message.channel.send('Hi ' + message.content[4:] + ", I'm Dad.")
        if message.content.startswith("im") or message.content.startswith("Im"):
            await message.channel.send('Hi ' + message.content[3:] + ", I'm Dad.")

def setup(bot):
    bot.add_cog(Dad(bot))