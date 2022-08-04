# Slackord 1.0 by Thomas Loupe

import datetime
from discord.ext import commands
import json
import time
from pathlib import Path
from TOKENS import bot_token
import discord
import datetime

HERE = Path(__file__).parent.resolve()

bot = commands.Bot(command_prefix="!")

MAIN = Path(
    "/home/lubianat/Downloads/No Budget Science Hack Week Slack export Jun 12 2020 - Aug 4 2022"
)


@bot.command(pass_context=True)
async def slack2discord(context):
    channel_name = "tema-dados"
    guild = context.message.guild
    await guild.create_text_channel(channel_name)
    NOW = MAIN.joinpath(channel_name)
    for channel in context.guild.channels:
        if channel.name == channel_name:
            wanted_channel_id = channel.id
    channel = bot.get_channel(wanted_channel_id)  # a specific channel

    filenames = [path.stem for path in NOW.glob("*.json")]
    filenames = sorted(
        filenames, key=lambda x: datetime.datetime.strptime(x, "%Y-%m-%d")
    )
    for filename in filenames:
        file_path = NOW.joinpath(f"{filename}.json")

        message_dict = json.loads(file_path.read_text())
        flag = 0
        last_user = ""
        for message in message_dict:
            if "user_profile" in message and "ts" in message:
                if flag == 0:
                    timestamp = message["ts"]
                    time = datetime.datetime.fromtimestamp(float(timestamp)).strftime(
                        "%Y-%m-%d"
                    )
                    await channel.send(f"===== {time} =====")

                flag = 1
            if "user_profile" in message and "text" in message:

                real_name = message["user_profile"]["real_name"]
                message_text = message["text"]
                if last_user == real_name:
                    message_to_send = message_text
                else:
                    message_to_send = f"**{real_name}** - {message_text}"
                    last_user = real_name
                await channel.send(message_to_send)


print("Running bot")
bot.run(bot_token)
