from font import Font, FontLoader

def getText():
    return 'Git'

class Font:
    def __init__(self):
        self.letters = {}

class FontLoader:
    def loadFont(self, directory):
        pass

class TextDrawer:
    def setFont(self, font):
        pass

    def draw(self, text):
        pass

text = getText()
font = FontLoader().loadFont('fancyFont/')

drawer = TextDrawer()
drawer.setFont(drawer)
font.draw(text)
