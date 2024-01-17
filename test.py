import os
import discord
from dotenv import load_dotenv
load_dotenv()

# reference https://discordpy.readthedocs.io/en/latest/index.html

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
client = discord.Client(intents=intents)
servers = {}


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    print(client.guilds) # this is me attempting to get the information to populate server setups and such still experimental
    print(client.get_guild(750781344329760799).owner) # working on retrieving who the owner is so that we can speak with them and provide the ability to allow them to control what happens with their channels



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # message.channel.name
    # print(f"Channel: {message.channel.name}, Channel ID {message.channel.id}, Category: {message.channel.category.name}, Server: {message.guild.name}")
    # print(type(message.channel.category.name))
    # currently this is all hardcoded basically because I need to work on the configuration files and find a better way of monitoring
    if message.channel.category.name == "Game Development" or message.channel.category.name == "Text Channels" or message.channel.category.name == "Minifantasy Multiverse":

        if message.channel.category.name == "Minifantasy Multiverse" and message.channel.name != "your-own-channel":
            await message.channel.move(beginning=True, offset=1)
            # print(f"{message.channel.position}")
            return
        await message.channel.move(beginning=True)
        # print(f"{message.channel.position}")


client.run(os.getenv('discord_api_secret'))
# invite link https://discord.com/api/oauth2/authorize?client_id=1189273205173649499&permissions=2419452944&scope=bot
