import discord
from discord.ext import commands

class CheckCog:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def broadcast(self, ctx):

        await ctx.send(ctx.channel)


def setup(bot):
    bot.add_cog(CheckCog(bot))
