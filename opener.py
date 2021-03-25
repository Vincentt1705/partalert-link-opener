#!usr/bin/env python3

"""
Currently only works with the PartAlert bot's embedded messages.

To be added if people want it:
  - Automatically open actual store pages
        (This will skip the partalert.net page but still include all affiliate links of PartAlert)
  - Option to disable certain websites
  - Support for #robynhood-alerts channel
"""

__author__ = "Vincentt1705 (Vincentt#1705 on Discord)"
__date__ = "25th of March 2021"
__version__ = "v0.1"

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
    "ps5"
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
                    if message.embeds:
                        embed = message.embeds[0]
                        embed_dict = embed.to_dict()
                        fields = embed_dict["fields"]

                        for field in fields:
                            if field["name"] == "Link":
                                url = field["value"]
                                open_link(url)
                                print_time(f"Link opened from #{message.channel.name}: '{url}'\n")


def main():
    client = DiscordLinkOpener("")
    client.remove_command("help")
    client.run(token, bot=False)


if __name__ == "__main__":
    sys.exit(main())