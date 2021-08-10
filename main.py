import discord
import requests
import json

client = discord.Client()

def get_bird_sound():
    response = requests.get("https://www.xeno-canto.org/api/2/recordings?query=cnt:brazil")
    json_data = json.loads(response.text)
    res = json_data
    print(res["recordings"][0]["url"])
    return(res["recordings"][0]["url"])

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

    if message.content.startswith('/sound'):
        sound = get_bird_sound()
        await message.channel.send(sound)

client.run('ODc0NzIwMDcxNDM4NzI5MjM3.YRLEjA._6CrhfiGt-o4ztvDSBGN6mQddLk')