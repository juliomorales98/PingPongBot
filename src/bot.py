import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

class PingPong(commands.Bot):
    def __init__(self):
        self.token = TOKEN
        super().__init__(commands.when_mentioned_or('>'))
        
bot = PingPong()

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=":ping_pong: Ping Pong Bot", description="Bot info", color=discord.Color.orange())
    embed.add_field(name="Info",value="Discord test bot, just send ping and bot should send pong response",inline = False)
    embed.add_field(name="Prefix",value=">", inline = False)
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    print("I'm ready to Pong")

bot.run(bot.token)
