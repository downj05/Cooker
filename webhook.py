import discord
from helpers import seconds_to_hms
import pyautogui as py
from typing import Tuple
from helpers import get_unturned_window_dimensions, focus_unturned_window
from game_functions import is_unturned_running
import info_tab
import os

class Webhook:
    def __init__(self, url, steam64, username):
        print("init webhook")
        self.NAME = f"Account Cooker | {info_tab.get_hostname()}"
        self.url = url
        self.webhook = discord.SyncWebhook.from_url(self.url)
        self.steam64 = steam64
        self.username = username

    @staticmethod
    def _screenshot(embed):
        if not is_unturned_running():
            print("Webhook._screenshot: Unturned is not running, using placeholder image")
            embed.add_field(name="Unturned is not running", value="No image preview available", inline=False)
            embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/b/b1/Missing-image-232x150.png")
            return embed, None
        focus_unturned_window()
        r = get_unturned_window_dimensions()

        # Convert the rectangle to a region
        region = (r[0], r[1], r[2] - r[0], r[3] - r[1])

        if not os.path.exists("bot_images"):
            print("Webhook._screenshot: Creating bot_images folder")
            os.mkdir("bot_images")

        py.screenshot('bot_images/screenshot.png', region=region)
        file = discord.File("bot_images/screenshot.png", filename="screenshot.png")
        embed.set_image(url="attachment://screenshot.png")
        return embed, file

    @staticmethod
    def _status_string(status_tuple: Tuple[int, int, int]) -> str:
        """
        Takes in a tuple of (time_in_game, total_time, cook_target) and returns a string
        :param status_tuple: tuple of (time_in_game, total_time, cook_target)
        :return: string
        """
        time_in_game, total_time, cook_target = status_tuple
        return f"Total time in game/on server: {seconds_to_hms(time_in_game)} | Total runtime: {seconds_to_hms(total_time)} | Target cooktime: {seconds_to_hms(cook_target)}"

    def warning(self, reason, status_tuple: Tuple[int, int, int]):
        embed=discord.Embed(title="Warning!", description="User left the server!", color=0xff7300)
        embed.set_author(name=self.NAME)
        embed, file = self._screenshot(embed)
        embed.add_field(name="Reason:", value=reason, inline=False)
        embed.set_footer(text=self._status_string(status_tuple=status_tuple))
        self._send(embed=embed, file=file)

    def error(self, traceback, status_tuple: Tuple[int, int, int]):
        embed=discord.Embed(title="Error!", description="Error during execution!", color=0xFF3C12)
        embed.set_author(name=self.NAME)
        embed, file = self._screenshot(embed)
        embed.add_field(name="Traceback:", value=traceback, inline=False)
        # embed.add_field(name="Next Steps:", value="Rejoining", inline=True)
        embed.set_footer(text=self._status_string(status_tuple=status_tuple))
        self._send(embed=embed, file=file)
    
    def ban(self, reason, status_tuple: Tuple[int, int, int]):
        embed=discord.Embed(title="Error!", description="User is banned from the server!", color=0xFF3C12)
        embed.set_author(name=self.NAME)
        embed, file = self._screenshot(embed)
        embed.add_field(name="Reason:", value=reason, inline=False)
        embed.set_footer(text=self._status_string(status_tuple=status_tuple))
        self._send(embed=embed, file=file)

    def success(self, status_tuple: Tuple[int, int, int]):
        embed=discord.Embed(title="Success!", description="User is done cooking!", color=0x07F614)
        embed.set_author(name=self.NAME)
        embed, file = self._screenshot(embed)
        embed.add_field(name=self._status_string(status_tuple=status_tuple), value="",  inline=False)
        self._send(embed=embed, file=file)


    def info(self, status_tuple: Tuple[int, int, int], rejoins_session: int, message:str=""):
        embed=discord.Embed(title=f"Info: {message}", description=message, color=0x00D0FF)
        embed.set_author(name=self.NAME)
        embed, file = self._screenshot(embed)
        embed.add_field(name=self._status_string(status_tuple=status_tuple), value=f"User has rejoined {rejoins_session} times",  inline=False)
        self._send(embed=embed, file=file)

    def test(self):
        embed=discord.Embed(title="Test!", description="This is a test of the Cookers webhook feature!", color=0x919191)
        embed.set_author(name=self.NAME)


        embed, file = self._screenshot(embed)

        # embed.set_footer(text="If you are seeing this, then it worked!")
        self._send(embed=embed, file=file)
    
    def _send(self, embed: discord.Embed, file: discord.File = None):
        # if no footer on embed, put our own
        if embed.footer.text is None:
            embed.set_footer(text=f"Steam64: {self.steam64} Username: {self.username}")

        try:
            if file is None:
                self.webhook.send(embed=embed)
                return
            self.webhook.send(embed=embed, file=file)
            return
        except Exception as e:
            print("Webhook._send: Error sending webhook: ", e)
            return