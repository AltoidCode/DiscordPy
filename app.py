import discord
import random
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Load stuff from json
def load_jokes():
    with open('jokes.json', 'r') as file:
        data = json.load(file)
    return data["jokes"]
def load_quotes():
    with open('quotes.json', 'r') as file:
        data = json.load(file)
    return data["quotes"]
def loadfacts():
    with open('facts.json', 'r') as file:
        data = json.load(file)
    return data["facts"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
jokes = load_jokes()
quotes = load_quotes()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Ping'):
        await message.channel.send('Pong!')
    elif message.content.startswith('$joke'):
        joke = random.choice(jokes)
        await message.channel.send(joke)
    elif message.content.startswith('$roll'):
        dice_roll = random.randint(1, 6)
        await message.channel.send(f'You rolled a {dice_roll}!')
    elif message.content.startswith('$quote'):
        quote = random.choice(quotes)
        await message.channel.send(quote)
    elif message.content.startswith('$fact'):
        facts = random.choice(facts)
        await message.channel.send(facts)

client.run('DISCORD_TOKEN')

if token:
    client.run(token)
else:
    print("No token found. Please make sure to set the DISCORD_TOKEN in ur dotenv file")