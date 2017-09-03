import discord
from discord.ext import commands

class my:
    def __init__(self, bot):
        self.bot = bot
        self.sessions = set()
        
  @commands.command()
  async def math(self):
    "Test"
     5+3
