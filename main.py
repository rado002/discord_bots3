import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant

chatbot = GenericAssistant("""'intents.json'""") # load intents.json file

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def_on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$aibot'):
        # await message.channel.send('Hello!')
        pass # do nothing


client.run(MTEwNDM1NDYwOTE0MjcwMjA4MA.G2_Dfa.z4MXEihQJtlSUr0dNsVmgT-pPJr-JwuR77iM70)