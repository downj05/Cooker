import discord
from helpers import seconds_to_hms
import pyautogui as py
from typing import Tuple

class Webhook:
    def __init__(self, url):
        print("init webhook")
        self.NAME = "Account Cooker"
        self.url = url
        self.webhook = discord.SyncWebhook.from_url(self.url)

    @staticmethod
    def _screenshot(embed):
        py.screenshot('bot_images/screenshot.png')
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
        # embed.add_field(name="Next Steps:", value="Rejoining", inline=True)
        embed.set_footer(text=self._status_string(status_tuple=status_tuple))
        self.webhook.send(embed=embed, file=file)

    def error(self, reason, status_tuple: Tuple[int, int, int]):
        embed=discord.Embed(title="Error!", description="User is banned from the server!", color=0xFF3C12)
        embed.set_author(name=self.NAME)
        embed, file = self._screenshot(embed)
        embed.add_field(name="Reason:", value=reason, inline=False)
        # embed.add_field(name="Next Steps:", value="Rejoining", inline=True)
        embed.set_footer(text=self._status_string(status_tuple=status_tuple))
        self.webhook.send(embed=embed, file=file)
    
    def success(self, status_tuple: Tuple[int, int, int]):
        embed=discord.Embed(title="Success!", description="User is done cooking!", color=0x07F614)
        embed.set_author(name=self.NAME)
        embed, file = self._screenshot(embed)
        embed.add_field(name=self._status_string(status_tuple=status_tuple), value="",  inline=False)
        self.webhook.send(embed=embed, file=file)


    def info(self, status_tuple: Tuple[int, int, int], rejoins_session: int, message:str=""):
        embed=discord.Embed(title="Info!", description=message, color=0x00D0FF)
        embed.set_author(name=self.NAME)
        embed, file = self._screenshot(embed)
        embed.add_field(name=self._status_string(status_tuple=status_tuple), value=f"User has rejoined {rejoins_session} times",  inline=False)
        self.webhook.send(embed=embed, file=file)

    def test(self):
        embed=discord.Embed(title="Test!", description="This is a test of the Cookers webhook feature!", color=0x919191)
        embed.set_author(name=self.NAME)


        embed, file = self._screenshot(embed)

        embed.set_footer(text="If you are seeing this, then it worked!")
        self.webhook.send(embed=embed, file=file)