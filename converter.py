from font import Font, FontLoader
from textdrawer import TextDrawer

def getText():
    return 'Git'

class Font:
    def __init__(self):
        self.letters = {}

class FontLoader:
    def loadFont(self, directory):
        pass

text = getText()
font = FontLoader().loadFont('fancyFont/')

drawer = TextDrawer()
drawer.setFont(drawer)
font.draw(text)
