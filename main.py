import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

organik = ["daun","sayur","kulit pisang ambon"]
anorganik = ["plastik","besi","kabel"]

@bot.command()
async def pilih(ctx):
    await ctx.send('Masukkan sampah')

    msg = await bot.wait_for("message")

    if msg.content in organik: 
        await ctx.send("Masukkan dalam organik")
    elif msg.content in anorganik:
        await ctx.send("Masukkan dalam anorganik")
    else:
        await ctx.send("Jenis sampah belum bisa dikenali")

bot.run("MTE1NTgyODU1MzY2MTgwODcxMA.Gb-qAj.-MUPi--67fynmMaHJIiCt_y1Z1p0mgZ6dX7oak")