import discord
import requests
import json
import math
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True

client = discord.Client(intents=intents)

helloArr = ["привет", "ку", "Ку", "hi", "hello", "салам", "приветик"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(mem):
    for channel in mem.guild.channels:
        if channel.name == 'основной':
            await channel.send(mem.name + ",добро пожаловать")
@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    for arr in helloArr:
        if message.content == arr:
            await message.channel.send(content="ассалам алейкум", file=discord.File("i.jpg"))

    arrCommand = message.content.split(" ")

    if arrCommand[0] == "погода":
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={' '.join(arrCommand[1:])}&appid=a6756a7aff9564a61122501b4ad92a9b")
        jsondata = json.loads(r.text)
        temp = math.floor(jsondata["main"]["temp"] - 273.15)
        await message.channel.send(f" {temp} °C")

    if message.content == "новинки":
        r = requests.get("https://www.mvideo.ru/")
        bs = BeautifulSoup(r.text, "lxml")
        block = bs.find("ul", attrs={"class": "accessories-product-list"})
        for child in block.children:

client.run('ODI3NTA1MDA2NDY5OTcxOTgw.YGcAFw.TkmAChxmDH1hkezemuebeVBSDJY')