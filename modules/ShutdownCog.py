import discord
import subprocess

from discord.ext import commands


class ShutdownCog(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("shutdown"):
            subprocess.run(["systemctl", "shutdown", "now"])
            subprocess.run(["shutdown", "/s"])