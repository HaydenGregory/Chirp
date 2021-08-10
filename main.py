import discord
from discord.ext import commands
import requests
import json


client2 = commands.Bot(command_prefix= '!')
client = discord.Client()

def get_bird_fact_photo():
    response = requests.get("https://some-random-api.ml/animal/birb")
    json_data = json.loads(response.text)
    image = json_data
    return(image['image'] + ' ' + image['fact'])

def get_bird_fact():
    response = requests.get("https://some-random-api.ml/animal/birb")
    json_data = json.loads(response.text)
    res = json_data
    return(res['fact'])

def get_bird_photo():
    response = requests.get("https://some-random-api.ml/animal/birb")
    json_data = json.loads(response.text)
    image = json_data
    return(image['image'])


@client.event

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/hello'):
        await message.channel.send('Chirp!')

    if message.content.startswith('/bird'):
        response = get_bird_fact_photo()
        await message.channel.send(response)

    if message.content.startswith('/image'):
        photo = get_bird_photo()
        await message.channel.send(photo)

    if message.content.startswith('/fact'):
        fact = get_bird_fact()
        await message.channel.send(fact)

client.run('ODc0NzIwMDcxNDM4NzI5MjM3.YRLEjA.ySjX6KfOz870beIucgxR4q-pCj0')