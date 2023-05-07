import discord
from discord.ext import commands

TOKEN = "MTEwNDM1NDYwOTE0MjcwMjA4MA.G2_Dfa.z4MXEihQJtlSUr0dNsVmgT-pPJr-JwuR77iM70"  # Replace with your bot token

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='hello', help='Say hello to the bot.')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

bot.run(TOKEN)
