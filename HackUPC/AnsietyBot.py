import discord
import requests
import json
import random
from stay_alive import stay_alive
import os

client = discord.Client()

kitty_images = ["Kitty.jpg", "Kitty2.jpg", "Kitty3.jpg", "Kitty8.jpg"]
help_depress = []
inspire_words = ["inspire", "inspiration", "need idea", "empty brain", "Inspire", "Inspiration", "Need idea",
                 "Empty brain"]
bye_words = ["bye", "see u", "see you", "Bye", "See u", "See you"]
hello_words = ["hello", "hi", "Hello", "Hi"]
sad_words = ["sad", "depressed", "unhappy", "angry", "world hates me", "Sad", "Depressed", "Unhappy", "Angry",
             "World hates me", "feeling down", "Feeling down"]
bot_hello = ['Hi mate', 'How are u doing', 'Hello!!']
bot_bye = ["Bye bye, a pleasure to talk with you", 'Bye man', 'See u', 'See you soon']
starter_encourage = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person!",
    "sometimes world can be an hostile places, but u can go trough",
    "Nevermind men, u are more than u think"
]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


"""
def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements
    
"""


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Watching Kitties Videos'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if any(word in msg for word in inspire_words):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in bye_words):
        await message.channel.send(random.choice(bot_bye))

    if any(word in msg for word in hello_words):
        await message.channel.send(random.choice(bot_hello))

    if any(word in msg for word in sad_words):
        help_depress.append(1)
        # print(help_depress)
        if len(help_depress) % 3:
            kitty = random.choice(kitty_images)
            await message.channel.send(file=discord.File(kitty))
            await message.channel.send("Here u have a cute kittie, be happy")
        if len(help_depress) == 3:
            await message.channel.send('Mate, maybe u need a bit of help')
        if len(help_depress) == 5:
            await message.channel.send('I encourage you to search some help')
        if len(help_depress) == 8:
            await message.channel.send('I truly recommend you to search some help')
        if len(help_depress) >= 10:
            await message.channel.send(
                "Hey mate, u should try to search for some help, here i give u a helpful link: "
                "https://www.telecinco.es/informativos/salud/como-acceder-psicologo-seguridad-social"
                "-be5m_18_2967045152.html%22")
        else:
            await message.channel.send(random.choice(starter_encourage))


stay_alive()
client.run(os.getenv('TOKEN'))
