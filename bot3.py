import discord
from discord.ext import commands

TOKEN = "MTEwNDQxNjMyMDAxMjk1MTYyMw.GmJYu-.8spEw-wH94uodX12_Di8YFjZvaJLmqhx-Cdqew"  # Replace with your bot token

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



@bot.command(name='question1', help='Answer to frequently asked question 1.')
async def question1(ctx):
    response = "This is the answer to question 1."
    await ctx.send(response)

@bot.command(name='question2', help='Answer to frequently asked question 2.')
async def question2(ctx):
    response = "This is the answer to question 2."
    await ctx.send(response)



bot.run(TOKEN)
