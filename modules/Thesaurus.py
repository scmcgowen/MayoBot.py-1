import discord
import nltk
from discord.ext import commands


from nltk.corpus import wordnet as wn

class Thesaurus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def define(self, ctx, *words):
        word = ""

        for word_part in words:
            word = word + " " + word_part

        word = word.lstrip().rstrip()

        async with ctx.channel.typing():
            synsets = wn.synsets(word)

            print(synsets)

            embed = discord.Embed(title="Definition of '%s'" % word, color=0x35d2c2)

            for synset in synsets:
                lemmmas = ", ".join(synset.lemma_names(lang='eng'))
                lemmmas = lemmmas.replace("_", " ")
                embed.add_field(name='(%s) %s' % (synset.pos(), lemmmas), value=synset.definition(), inline=False)

            embed.set_footer(text="Requested by %s" % ctx.message.author.name)
            await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Thesaurus(bot))