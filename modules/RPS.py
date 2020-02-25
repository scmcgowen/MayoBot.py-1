import asyncio

from discord.ext import commands
from random import randrange


class RPS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx):
        await ctx.send("Okay. You start. Rock, Paper or Scissors?")

        def get_submission_of_bot() -> str:
            rand = randrange(3)
            if rand == 0:
                return 'ROCK'
            elif rand == 1:
                return 'PAPER'
            elif rand == 2:
                return 'SCISSORS'
            else:
                return 'ROCK'

        bot_submission = get_submission_of_bot()

        def check(m):
            if m.channel == ctx.channel and m.author == ctx.message.author:
                if m.content.upper() in ['ROCK', 'PAPER', 'SCISSORS']:
                    return True
                return False
            return False

        try:
            message = await self.bot.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.message.channel.send('👎 | Aborting RockPaperScissors due to you not being able to answer >:c')
        else:
            if bot_submission == message.content.upper():
                await ctx.send("I also chose '%s'! It's a draw! Congrats to us both!" % message.content)
            else:
                if bot_submission == 'ROCK' and message.content.upper() == 'PAPER':
                    await ctx.send("I chose Rock and you chose Paper - you win!")
                elif bot_submission == 'PAPER' and message.content.upper() == 'ROCK':
                    await ctx.send("I chose Paper and you chose Rock - I win!")
                elif bot_submission == 'SCISSORS' and message.content.upper() == 'PAPER':
                    await ctx.send("I chose Scissors and you chose Paper - I win!")
                elif bot_submission == 'PAPER' and message.content.upper() == 'SCISSORS':
                    await ctx.send("I chose Paper and you chose Scissors - you win!")


def setup(bot):
    bot.add_cog(RPS(bot))
