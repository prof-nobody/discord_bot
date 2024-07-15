import datetime
import os
import discord
from discord.ext import tasks
from dotenv import load_dotenv
load_dotenv()

# reference https://discordpy.readthedocs.io/en/latest/index.html

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.minifantasy = 745121447839662152

    # start the task to run in the background
    async def setup_hook(self) -> None:
        self.check_last_messages.start()

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        # print(client.guilds)
        print('----')
        self.minifantasy = self.get_guild(745121447839662152)
        print(self.minifantasy.categories[5])

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.channel.category.name == "Game Development" or message.channel.category.name == "Text Channels" or message.channel.category.name == "Minifantasy Multiverse":

            if message.channel.category.name == "Minifantasy Multiverse" and message.channel.name != "your-own-channel":
                await message.channel.move(beginning=True, offset=1)
                # print(f"{message.channel.position}")
                return
            await message.channel.move(beginning=True)
            # print(f"{message.channel.position}")


    @tasks.loop(hours=24)
    async def check_last_messages(self):
        multiverse_id = 847317904877289514
        # get the datetime for one year ago, we can see the last time someone posted in a channel
        one_year_ago = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=365)

        for channel in self.minifantasy.channels:
            # print(channel.category_id)
            # print(type(channel.category_id))
            if channel.category_id == multiverse_id:
                # print(channel.name)
                async for message in channel.history(limit=1):
                    if message.created_at < one_year_ago:
                        print(f"{message.channel}'s last message was {message.created_at}")
                        await channel.edit(category=self.minifantasy.categories[5], reason="Channel has had no activity in the last year")
                    # print(f"Message Timestamp {message.created_at} and it shouldn't be older than {one_year_ago}")
                    # print(f"Channel: {message.channel} {message.id} {message.created_at}")




    @check_last_messages.before_loop
    async def before_check_last_messages(self):
        await self.wait_until_ready()


client = MyClient(intents=intents)
client.run(os.getenv('discord_api_secret'))