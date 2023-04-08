from requests import *
from z.rnd import *

def SystemD(webhook):
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
                    "value": f"`{phwid}`",
                    "inline": True
                },
                {
                    "name": "Disk:",
                    "value": f"`{disk}gb`",
                    "inline": True
                },
                ],
            "footer": {
                "text": f"{oembed} · System Information · {vbv}",
                "icon_url": f"{pfpembed}"
                },
            }
        ],
        "avatar_url": f"{pfpembed}",
        "username": f"{oembed}",
        "attachments": []
        }

    post(webhook, json=SystemInfo)
