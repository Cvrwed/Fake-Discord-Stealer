from string import ascii_letters, digits;from random import randint, choice, SystemRandom
from requests import post, get;from pystyleclean import *
from base64 import b64encode
from faker import Faker
from randmac import RandMac

System.Clear()
Cursor.HideCursor()
System.Title("Fake Grabber")

x = Faker()
step1 = "=="
step1.find("==") != 1
tokenid = str(randint(000000000000000000, 999999999999999999))
step2 = tokenid.encode("ascii")
finalstep = b64encode(step2)
step1 = finalstep.decode("ascii")

## Fake token
token = step1+"."+choice(ascii_letters).upper()+''.join(choice(ascii_letters + digits) for _ in range(6))+"."+''.join(choice(ascii_letters + digits) for _ in range(38))

## Fake phone
phone = "+1 "+"("+"".join(str(randint(0, 9)) for _ in range(3)) + ")" + "-" + "".join(str(randint(0, 9)) for _ in range(3))+ "-" + "".join(str(randint(0, 9)) for _ in range(4))

## Fake Ip
ipfake = x.ipv4()

## Fake Geo
latitud = x.latitude()
longitud = x.longitude()

## Random True or False
gay = choice([False, False, False, False, False, True])
gay2 = choice([True, True, True, True, True, False])

## Fake OS
fakeos = choice(['Windows', 'Mac', 'Linux', 'IOS', 'Unknown'])

## Fake Mac
fakemac = RandMac()

## Found
fcookies = randint(1,999)
fpass = randint(1, 999)
friends = randint(1, 1000)

## Random badges
rarebadge = choice([
    "<:developer:874750808472825986> ",
    "<:bughunter_2:874750808430874664> ",
    "<:early_supporter:874750808414113823> ",
    "<:bughunter_1:874750808426692658> ",
    "<:hypesquad_events:874750808594477056> ",
    "<:partner:874750808678354964> ",
    "<:staff:874750808728666152> "])

comunbadge = choice([
    "<:balance:874750808267292683> ",
    "<:brilliance:874750808338608199> ",
    "<:bravery:874750808388952075> "])

## email fake
f1 = x.first_name()
number = randint(0000, 9999)
e1 = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
e2 = choice(e1)
email = f"{f1}.{number}@{e2}"

## Random User

# Credits to itschasa
user = (choice(get("https://raw.githubusercontent.com/itschasa/Discord-Scraped/main/names.txt").text.split("\n")))
tag = randint(1111, 9999)

## System

n1 = randint(0, 9) # numbers 
n2 = randint(00, 99) # 2 numbers 
n3 = randint(00000, 99999) # 5 numbers 

l1 = ''.join(SystemRandom().choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) # letters 
l2 = ''.join(SystemRandom().choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(2)) # 2 letters
l3 = ''.join(SystemRandom().choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3)) # 3 letters
l4 = ''.join(SystemRandom().choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4)) # 4 letters

ram = randint(4, 32)
disk = randint(1024, 9999)
hwid = f"{n2}{l1}{n2}{l3}-{n2}{l1}{n1}-{n2}{l1}{n1}-{n1}{l1}{n2}-{n1}{l1}{n3}{l2}{n2}{l1}"
#winkey = f"{l4}{n1}-{l1}{n1}{l3}-{l3}{n2}-{n1}{l1}{n1}{l2}-{n1}{l3}{n1}"



def send(webhook):
    Info = {
        "content": f'',
        "embeds": [
            {
            "color": 2303786,
            "fields": [  
                {
                    "name": "ID:",
                    "value": f"`{tokenid}`",
                    "inline": True
                },
                {
                    "name": "Email:",
                    "value": f"`{email}`",
                    "inline": True
                },
                {
                    "name": "Phone:",
                    "value": f"`{phone}`",
                    "inline": True
                },
                {
                    "name": "2FA:",
                    "value": f"`{gay}`",
                    "inline": True
                },
                {
                    "name": "IP:",
                    "value": f"`{ipfake}`",
                    "inline": True
                },
                {
                    "name": "Badges:",
                    "value": f"{comunbadge}{rarebadge}",
                    "inline": True
                },
                                    {
                    "name": "Latitud - Longitud:",
                    "value": f"`{latitud} {longitud}`",
                    "inline": True
                },
                {
                    "name": "Token:",
                    "value": f"```{token}```",
                }
                ],
            "author": {
                "name": f"{user}#{tag}",
                "icon_url": "https://media.tenor.com/noyn9bef3O8AAAAd/zerotwo-dance.gif"
            },
            "footer": {
                "text": "Fake Grabber · Discord Information",
                "icon_url": "https://media.tenor.com/noyn9bef3O8AAAAd/zerotwo-dance.gif"
                },
            "thumbnail": {}
            }
        ],
        "avatar_url": "https://media.tenor.com/noyn9bef3O8AAAAd/zerotwo-dance.gif",
        "username": "Fake Grabber",
        "attachments": []
        }
    
    post(webhook,json=Info)

def send2(webhook):
    SystemInfo = {
        "embeds": [
            {
            "color": 2303786,
            "fields": [  
                {
                    "name": "Os:",
                    "value": f"`{fakeos}`",
                    "inline": True
                },
                {
                    "name": "Mac:",
                    "value": f"`{fakemac}`",
                    "inline": True
                },
                {
                    "name": "Ram:",
                    "value": f"`{ram}gb`",
                    "inline": True
                },
                {
                    "name": "Hwid:",
                    "value": f"`{hwid}`",
                    "inline": True
                },
                {
                    "name": "Disk:",
                    "value": f"`{disk}gb`",
                    "inline": True
                },
                ],
            "footer": {
                "text": "Fake Grabber · System Information",
                "icon_url": "https://media.tenor.com/noyn9bef3O8AAAAd/zerotwo-dance.gif"
                },
            }
        ],
        "avatar_url": "https://media.tenor.com/noyn9bef3O8AAAAd/zerotwo-dance.gif",
        "username": "Fake Grabber",
        "attachments": []
        }

    post(webhook, json=SystemInfo)

webhook = input(" Ingresa tu webhook > ")
send(webhook)
send2(webhook)
Write.Print(" Mensaje enviado\n", interval=0.05, hide_cursor=True, color=Colors.white)
