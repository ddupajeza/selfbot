import discord
from discord.ext import commands
import asyncio

class my:
    def __init__(self, bot):
        self.bot = bot
        self.sessions = set()
        
  @commands.command()
  async def math(self):
    "Test"
    randnum = random.randint(0,1)
        if randnum == 0:
            coin = 'Head'
        else:
            coin = 'Tail'
        emb = discord.Embed(color=discord.Color.gold(), title="You Flipped A...", description = coin)
        await self.bot.say('', embed = emb)

 def setup(bot):
    bot.add_cog(my(bot))
