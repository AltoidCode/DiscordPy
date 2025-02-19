import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Ping'):
        await message.channel.send('Pong!')

client.run('MTM0MTkxNDM3NTQzMDM0NDczNQ.G5ulAP.LkZzg_BvGKHmwURAA-bejqNap515LTGE_tR71E')