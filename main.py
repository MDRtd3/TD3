import discord
import os
from discord.ext.commands.core import command
from discord.flags import Intents
import requests
from decouple import config
from discord import activity
from discord.ext import commands


bot = commands.Bot(command_prefix="!", Intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Estou pronto!")
    activity = discord.Game(name="patata")
    await bot.change_presence(status=discord.Status.idle, activity=activity)



def load_cogs(bot):
    bot.load_extension("manager")


load_cogs(bot)



TOKEN = config("TOKEN")
bot.run(TOKEN)
