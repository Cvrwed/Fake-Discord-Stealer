from pystyleclean import *
def banner():
    try:
        f  = open("x/banner.rat","r",encoding="utf8")
        ascii = "".join(f.readlines())
        print(Anime.Fade(Center.XCenter(ascii), Colors.red_to_black, Colorate.Vertical, enter=True))
    except KeyboardInterrupt:
        exit()

def banner2():
    try:
        f2  = open("x/banner2.rat","r",encoding="utf8")
        ascii2 = "".join(f2.readlines())
        print(Colorate.Vertical(Colors.DynamicMIX((Col.red, Col.black)), Center.XCenter(ascii2)))
    except KeyboardInterrupt:
        exit()