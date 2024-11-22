import discord
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
discordToken = getenv("DISCORD_TOKEN")
GPTToken = getenv("GPT_TOKEN")

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

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(discordToken)
