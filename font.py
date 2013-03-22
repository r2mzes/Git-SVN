class Font:
    pass

class FontLoader:
    def loadFont(self, directory):
        font = Font("fancy")
		return font


class Font:
    def __init__(self, name):
        self.name = name
        self.letters = {}
