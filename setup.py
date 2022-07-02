from pygame import *
from random import *
font.init()

scale = 1
up = int(720 * scale)
wid = int(1080 * scale)
window = display.set_mode((wid, up))
display.set_caption('Пинг-понг')
