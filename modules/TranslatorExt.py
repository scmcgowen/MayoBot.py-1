import discord
from discord.ext import commands
from googletrans import Translator


class TranslatorExt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def translate(self, ctx, dest, *msgs):
        msg = ""
        for msg_part in msgs:
            msg = msg + " " + msg_part

        msg = msg.lstrip().rstrip()

        translator = Translator()
        translated = translator.translate(msg, dest=dest)

        target_lang = translated.dest
        origin_lang = translated.src

        origin_lang = origin_lang.replace('en', 'gb').replace('ja', 'jp')
        target_lang = target_lang.replace('ja', 'jp').replace('en', 'gb')

        embed = discord.Embed(title="Translation", description=":flag_%s: ➡ :flag_%s:" % (origin_lang, target_lang), color=0x0080ff)
        embed.add_field(name="Original: :flag_%s:" % origin_lang, value=translated.origin, inline=False)
        embed.add_field(name="Translated: :flag_%s:" % target_lang, value=translated.text, inline=False)
        embed.set_footer(text="Source: Google Translator")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(TranslatorExt(bot))