import discord
import requests

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.typing = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if "linux" in message.content.lower().strip() and not message.author.bot:
        print("Detected 'linux' in message")
        text = "I'd just like to interject for a moment. What you're refering to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.\n\nMany computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called Linux, and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.\n\nThere really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called Linux distributions are really distributions of GNU/Linux!"
        print("Sending message")
        await message.channel.send(text)

    elif "fox" in message.content.lower().strip() and not message.author.bot:
        print ("Detected 'fox' in message")
        anipic = requests.get("https://api.tinyfox.dev/img?animal=fox&json")
        print ("Sending fox picture")
        await message.channel.send(f"https://api.tinyfox.dev{anipic.json()['loc']}")

    elif any(word in message.content.lower().strip() for word in ["yeen", "hyena"]) and not message.author.bot:
        print ("Detected 'yeen' or 'hyena' in message")
        anipic = requests.get("https://api.tinyfox.dev/img?animal=yeen&json")
        print ("Sending hyena picture")
        await message.channel.send(f"https://api.tinyfox.dev{anipic.json()['loc']}")

    elif any(word in message.content.lower().strip() for word in ["possum", "poss"]) and not message.author.bot:
        print ("Detected 'possum' or 'poss' in message")
        anipic = requests.get("https://api.tinyfox.dev/img?animal=poss&json")
        print ("Sending possum picture")
        await message.channel.send(f"https://api.tinyfox.dev{anipic.json()['loc']}")

    elif any(word in message.content.lower().strip() for word in ["bun", "bunny"]) and not message.author.bot:
        print ("Detected 'bun' or 'bunny' in message")
        anipic = requests.get("https://api.tinyfox.dev/img?animal=bun&json")
        print ("Sending bunny picture")
        await message.channel.send(f"https://api.tinyfox.dev{anipic.json()['loc']}")

    elif any (word in message.content.lower().strip() for word in ["marten", "pine marten"]) and not message.author.bot:
        print ("Detected 'marten' or 'pine marten' in message")
        anipic = requests.get("https://api.tinyfox.dev/img?animal=marten&json")
        print ("Sending marten picture")
        await message.channel.send(f"https://api.tinyfox.dev{anipic.json()['loc']}")
   
    elif any (word in message.content.lower().strip() for word in ["dog", "doggy", "puppy"]) and not message.author.bot:
        print ("Detected 'dog,' 'doggy' or 'puppy' in message")
        anipic = requests.get("https://api.tinyfox.dev/img?animal=dog&json")
        print ("Sending dog picture")
        await message.channel.send(f"https://api.tinyfox.dev{anipic.json()['loc']}")

    elif any (word in message.content.lower().strip() for word in ["deer", "forest puppy"]) and not message.author.bot:
        print ("Detected 'deer' or 'forest puppy' in message")
        anipic = requests.get("https://api.tinyfox.dev/img?animal=bleat&json")
        print ("Sending deer picture")
        await message.channel.send(f"https://api.tinyfox.dev{anipic.json()['loc']}")

client.run('BOT_TOKEN_HERE')
