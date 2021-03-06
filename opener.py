#!usr/bin/env python3

"""
WARNING: SELF-BOTTING IS AGAINST DISCORD TOS AND THERE IS THE 
    POSSIBILITY TO GET BANNED FOR IT EVEN IF THE CHANCE IS LOW!
    Using this script is at your own risk!

Currently only works with the PartAlert bot's embedded messages.

You can always request features, just send a message on Discord.
"""

__author__ = "Vincentt1705 (Vincentt#1705 on Discord)"
__date__ = "10th of June 2021"
__version__ = "v0.1.5"

import sys
import webbrowser
from discord.ext.commands import Bot
from datetime import datetime

# Add your personal authorization token here
token = ""

# Remove all roles that you don't want to open links from
roles = ["EU", "UK", "DE", "FR", "IT", "ES", "NL", "BE", "PL"]

# The script will only see messages from channels you're in since it's bound to your account.
# You don't have to do anything here unless you don't want to open links from a channel you ARE in.
channels = [
    "founders-edition",
    "rtx3060",
    "rtx3060ti",
    "rtx3070",
    "rtx3080",
    "rtx3090",
    "rx6700xt",
    "rx6800",
    "rx6800xt",
    "rx6900xt",
    "ryzen5600x",
    "ryzen5800x",
    "ryzen5900x",
    "ryzen5950x",
    "xbox",
    "ps5",
    "i5-11400",
    "i5-11500",
    "i5-11600",
    "i7-11700",
    "i9-11900"
]


def print_time(*content):
    """
    Can be used as a normal print function but includes the current date and time
    enclosed in brackets in front of the printed content.

    :param content: The content you would normally put in a print() function
    """
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"[{date_time}]", *content)


def open_link(url):
    webbrowser.open(url)


class DiscordLinkOpener(Bot):
    async def on_ready(self):
        print_time(f"Discord Link Opener is ready through user {str(self.user)}")

        if len(roles) == 0:
            print(f"\tListening for messages in {len(channels)} channels with any region role tag\n")
        else:
            print(f"\tListening for messages in {len(channels)} channels "
                  f"that are tagged with one (or more) of the following region roles: {', '.join(roles)}\n")

    async def on_message(self, message):
        if message.guild:
            if message.guild.id == 768363408109469697 and message.channel.name in channels:
                if any(tagged_role.name in roles for tagged_role in message.role_mentions):
                    # Override the message to be able to read the embeds (FIX)
                    message = await self.get_last_msg(message.channel.id)
                    if message.embeds:
                        embed = message.embeds[0]
                        embed_dict = embed.to_dict()
                        fields = embed_dict["fields"]

                        for field in fields:
                            if field["name"] == "Link":
                                url = field["value"]

                                open_link(url)
                                print_time(f"Link opened from #{message.channel.name}: '{url}'\n")
                  
    async def get_last_msg(self, channel_id):
        """
        Fix to make reading embeds possible

        :param channel_id: The id of the channel you want the latest message from.
        :return: The latest message in the given channel.
        """
        msg = await self.get_channel(channel_id).history(limit=1).flatten()
        return msg[0]                


def main():
    client = DiscordLinkOpener("")
    client.remove_command("help")
    client.run(token, bot=False)


if __name__ == "__main__":
    sys.exit(main())
