from string import ascii_letters, digits, ascii_uppercase;from random import randint, choice, SystemRandom
from base64 import b64encode
from faker import Faker
from randmac import RandMac
from requests import get
from datetime import datetime

now = datetime.now()
x = Faker()

step1 = b64encode(str(randint(000000000000000000, 999999999999999999)).encode("ascii")).decode("ascii")
tokenid = str(randint(000000000000000000, 999999999999999999))
## Fake token
token = step1+"."+choice(ascii_letters).upper()+''.join(choice(ascii_letters + digits) for _ in range(6))+"."+''.join(choice(ascii_letters + digits) for _ in range(38))

## ?
vbv = now.strftime("%H:%M")

## Fake phone
phone = "+1 "+"("+"".join(str(randint(0, 9)) for _ in range(3)) + ")" + "-" + "".join(str(randint(0, 9)) for _ in range(3))+ "-" + "".join(str(randint(0, 9)) for _ in range(4))

## Fake Ip
ipfake = x.ipv4()

## Fake Geo
latitud = x.latitude()
longitud = x.longitude()

## Random True or False
gay = bool(choice([0, 0, 0, 0, 0, 1]))
#gay2 = choice([True, True, True, True, True, False])

## Fake OS
fakeos = choice(['Windows', 'Mac', 'Linux', 'IOS', 'Unknown'])

## Fake Mac
fakemac = RandMac()

## Found
fcookies = randint(1,999)
fpass = randint(1, 999)
#friends = randint(1, 1000)

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
email = f"{f1}.{randint(0000, 9999)}@{choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'])}"

## Random User

# Credits to itschasa
user = (choice(get("https://raw.githubusercontent.com/itschasa/Discord-Scraped/main/names.txt").text.split("\n")))
tag = randint(0001, 9999)

## System

n1 = randint(0, 9)
n2 = randint(00, 99)
n3 = randint(00000, 99999) # numbers 

l1 = ''.join(SystemRandom().choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) # letters 
l2 = ''.join(SystemRandom().choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(2)) # 2 letters
l3 = ''.join(SystemRandom().choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3)) # 3 letters
l4 = ''.join(SystemRandom().choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4)) # 4 letters

ram = randint(4, 32)
disk = randint(10, 999)
hwid = f"{n2}{l1}{n2}{l3}-{n2}{l1}{n1}-{n2}{l1}{n1}-{n1}{l1}{n2}-{n1}{l1}{n3}{l2}{n2}{l1}"
#winkey = f"{l4}{n1}-{l1}{n1}{l3}-{l3}{n2}-{n1}{l1}{n1}{l2}-{n1}{l3}{n1}"

## Browser Data

rBrowser = choice(["Chrome", "Brave", "Opera", "Firefox", "Safari", "Microsoft Edge"])
Visa = randint(4000000000000000,4999999999999999)
Mastercard = randint(5000000000000000,5999999999999999)
Discover = randint(6000000000000000,6999999999999999)
Month = randint(1, 12)
Year =randint(2023, 2031)
Cvv = randint(000, 999)
cc = choice([Visa, Mastercard, Discover])
cc2 = f"|{Month}|{Year}|{Cvv}"

## Roblox
rcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"+choice(digits)+''.join(choice(ascii_uppercase + digits) for _ in range(744))
ruser = (choice(get("https://raw.githubusercontent.com/zEncrypte/rblx-usernames/master/names.txt").text.split("\n")))
robux = randint(0, 99)
friends = randint(0, 50)
rpssw = (choice(get("https://gist.githubusercontent.com/cihanmehmet/68abd1a11b3477ebd30eea7ef23183b5/raw/c06ff4cb95e3cc6679d3cd74f24617f498158f9e/password-wordlist.txt").text.split("\n")))
