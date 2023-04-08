from string import ascii_letters, digits, ascii_uppercase;from random import randint, choice, SystemRandom
from base64 import b64encode;from faker import Faker
from randmac import RandMac
from requests import get
from datetime import datetime
from .hwid import *
from .phones import *

now = datetime.now()
x = Faker()

## Fake token
step1 = b64encode(str(randint(000000000000000000, 999999999999999999)).encode("ascii")).decode("ascii")
tokenid = str(randint(000000000000000000, 999999999999999999))
token = step1+"."+choice(ascii_letters).upper()+''.join(choice(ascii_letters + digits) for _ in range(6))+"."+''.join(choice(ascii_letters + digits) for _ in range(38))

## time
vbv = now.strftime("%H:%M")

## Random phone 
phone = choice([us, colombia, venezuela, mexico, chile, ecuador, elsalvador, guatemala, honduras, nicaragua])

## Fake Ip (Only US)
ipfake = x.ipv4()

## Fake Geo
latitud = x.latitude()
longitud = x.longitude()

## Random True or False
gay = bool(choice([0, 0, 0, 0, 0, 1]))

## Fake OS
fakeos = choice(['Windows', 'Mac', 'Linux', 'IOS', 'Unknown'])

## Fake Mac
fakemac = RandMac()

## Found
fcookies = randint(1,999)
fpass = randint(1, 999)

## msg
oembed = "Nazi Token Grabber"
pfpembed = "https://media.discordapp.net/attachments/917748345429192784/927010571688218694/coolgifwow.gif"

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
user = (choice(get("https://raw.githubusercontent.com/itschasa/Discord-Scraped/main/names.txt").text.split("\n")))
tag = randint(0x000, 9999)

## System
ram = randint(4, 32)
disk = randint(10, 999)

## Hwid
phwid = f"{H1}{H2}{H3}{H4}{H5}{H6}{H7}{H8}{H9}{H10}{H11}{H12}{H13}{H14}{H15}{H16}{H17}{H18}{H19}{H20}{H21}{H22}{H23}{H24}{H25}{H26}{H27}{H28}{H29}{H30}{H31}{H32}{H33}{H34}{H35}{H36}{H37}"

## Browser Data
rBrowser = choice(["Chrome", "Brave", "Opera", "Firefox", "Safari", "Microsoft Edge", "Yandex"])
Visa = randint(4000000000000000,4999999999999999)
Mastercard = randint(5000000000000000,5999999999999999)
Discover = randint(6000000000000000,6999999999999999)
Month = randint(1, 12)
Year =randint(2023, 2031)
Cvv = randint(000, 999)
cc = choice([Visa, Mastercard, Discover])
cc2 = f"|{Month}|{Year}|{Cvv}"

## Roblox Data
rcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"+choice(digits)+''.join(choice(ascii_uppercase + digits) for _ in range(744))
ruser = (choice(get("https://raw.githubusercontent.com/zEncrypte/rblx-usernames/master/names.txt").text.split("\n")))
robux = randint(0, 99)
friends = randint(0, 50)
rpssw = (choice(get("https://gist.githubusercontent.com/cihanmehmet/68abd1a11b3477ebd30eea7ef23183b5/raw/c06ff4cb95e3cc6679d3cd74f24617f498158f9e/password-wordlist.txt").text.split("\n")))
