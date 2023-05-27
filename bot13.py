import discord
from discord.ext import commands

TOKEN = "MTEwNDYwOTQ5NDEwMjcyMDUyMw.GXpduw.-9nuogjZ2LnT1sB04LAgcUh6mmd-em96SLNXq4"  # Replaced with own bot token

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
# intents.members = True
# intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# New command: hello
@bot.command(name='hello', help='Say hello to the bot.')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')


# New command: add
@bot.command(name='add', help='Add two numbers. Usage: !add <num1> <num2>')
async def add(ctx, num1: float, num2: float):
    result = num1 + num2
    await ctx.send(f'The sum of {num1} and {num2} is {result}')


# New command: multiply
@bot.command(name='multiply',
             help='Multiply two numbers. Usage: !multiply <num1> <num2>')
async def multiply(ctx, num1: float, num2: float):
    result = num1 * num2
    await ctx.send(f'The product of {num1} and {num2} is {result}')

# New command: feber
@bot.command(name='feber', help='help to feber')
async def feber(ctx):
    await ctx.send(f'paracet, ibux, eller varm te med sitron og honning {ctx.author.mention}!')

# New command: mage
@bot.command(name='mage', help='help to mage')
async def mage(ctx):
    await ctx.send(f'priobiotiker, eller hva noeyaktig?... {ctx.author.mention}!')


bot.run(TOKEN)
