import requests
from bs4 import BeautifulSoup
import csv

# import discord
# from discord.ext import commands
# import asyncio
# import json
# import os
# import random
# import traceback

# TOKEN = 'MTEwNDgwMTgzNTMxNjk1MzIxOQ.GmowO4._hbzbW7Y7BbegsEotwUBF9g-0vXvo-oIdEpUHQ'

# intents = discord.Intents.default()
# intents.typing = False
# intents.presences = False

# bot = commands.Bot(command_prefix='!', intents=intents)


# @bot.event
# async def on_ready():
#   print(f'{bot.user.name} has connected to Discord!')


# @bot.command(name='hello', help='Say hello to the bot.')
# async def hello(ctx):
#   await ctx.send(f'Hello {ctx.author.mention}!')

def scrape_paragraphs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all('p')

    return [p.text for p in paragraphs]

URL = "https://www.dittapotek.no/c/munn--og-tannpleie/a/A50002"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
   
quotes=[]  # a list to store quotes

# table = soup.find('div') 
table = soup.find('div', attrs = {'id':'all_quotes'}) 
   
for row in table.findAll('div',
                         attrs = {'class':'js-shortcut-section'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)


# webpage = requests.get('https://quotes.toscrape.com/')

filename = 'Bot001.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)

# print(webpage.content)

# with open("Bot001.txt", "w", encoding="utf-8") as f:
#     for paragraph in p:
#         f.write(paragraph + "\n\n")



# @client.event
# async def on_ready():
#   print('Logged in as')
#   print(client.user.name)
#   print(client.user.id)
#   print('------')

bot.run(TOKEN)
