from string import ascii_letters, digits;from random import randint, choice
from requests import post;from pystyleclean import *
from base64 import b64encode
from faker import Faker
from randmac import RandMac


System.Clear()
Cursor.HideCursor()
System.Title("Fake Grabber")

class FakeGrabber():
    def __init__(self):
        self.userinput()

    def userinput(self):
        __WEBHOOK__ = input(" Ingresa tu webhook > ")
        self.send(__WEBHOOK__)

    def getinfo(self):
        
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
        faker = Faker()
        Ipfake = faker.ipv4()

        ## Fake Geo

        faker = Faker()
        latitud = faker.latitude()
        longitud = faker.longitude()

        ## Random True or False

        gay = choice([False, False, False, False, False, True])
        gay2 = choice([True, True, True, True, True, False])

        ## Fake OS
        fakeos = choice(["Windows", "Linux", "MacOS X"])

        ## Fake Mac

        fakemac = RandMac()

        ## Cookies Found
        fcookies = randint(1,999)
        fpass = randint(1, 999)
        friends = randint(1, 1000)
        servers = randint(1, 200)

        return fakeos, Ipfake, fakemac, latitud, longitud, gay, gay2, phone, friends, tokenid, fcookies, fpass, servers, token
    def send(self, __WEBHOOK__):
        fakeos, Ipfake, fakemac, latitud, longitud, gay, gay2, phone, friends, tokenid, fcookies, fpass, servers, token = self.getinfo()
        
        embed = {"content": '', 
            "embeds": [{  
                "color": 1051660, 
                "fields": [{ 
                    "name": "OS", 
                    "value": f"{fakeos}", 
                    "inline": True }, { 
                        "name": "Ip", 
                        "value": f"{Ipfake}", 
                        "inline": True }, { 
                            "name": "Mac", 
                            "value": f"{fakemac}", 
                            "inline": True }, { 
                                "name": "Latitud", 
                                "value": f"{latitud}", 
                                "inline": True }, { 
                                    "name": "Longitud", 
                                    "value": f"{longitud}", 
                                    "inline": True }, { 
                                        "name": "Nitro",
                                          "value": f"{gay}", 
                                          "inline": True }, { 
                                            "name": "Expire in", 
                                            "value": f"N/A", 
                                            "inline": True }, { 
                                                "name": "Phone", 
                                                "value": f"{phone}", 
                                                "inline": True }, { 
                                                    "name": "2FA", 
                                                    "value": f"{gay2}", 
                                                    "inline": True }, { 
                                                        "name": "Friends Amount", 
                                                        "value": f"{friends}", 
                                                        "inline": True }, { 
                                                            "name": "ID", 
                                                            "value": f"{tokenid}", 
                                                            "inline": True }, { 
                                                                "name": "Cookies Amount", 
                                                                "value": f"{fcookies}", 
                                                                "inline": True }, { 
                                                                    "name": "Passwords Amount", 
                                                                    "value": f"{fpass}", 
                                                                    "inline": True }, { 
                                                                        "name": "Servers Amount", 
                                                                        "value": f"{servers}", 
                                                                        "inline": True }, { 
                                                                            "name": "Token", 
                                                                            "value": f"```fix\n{token}\n```" }], 
                                                                            "footer": { "text": f"Made by Bipas Gang" }, 
                                                                            "thumbnail": {
                                                                                "url": f"https://media.tenor.com/noyn9bef3O8AAAAd/zerotwo-dance.gif"}}], 
                                                                                "username": f"Bipas", 
                                                                                "avatar_url": f"https://cdn.discordapp.com/attachments/1022628482154512384/1060932284653522964/19ffbb7345edceca0713b862147bc120.png", 
                                                                                "attachments": [] }
        post(__WEBHOOK__,json=embed)

if __name__ == "__main__":
    FakeGrabber()

