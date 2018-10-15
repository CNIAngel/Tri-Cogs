import discord
from discord.ext import commands

class BroadcastCog:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def broadcast(self, chnl : str, *, message :str ):
        channel = chnl

        await channel.send(message)


def setup(bot):
    bot.add_cog(BroadcastCog(bot))
