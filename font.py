class Font:
    pass

class FontLoader:
    def loadFont(self, directory):
        font = Font("fancy")
		
        font.letters['G'] = r'''
  ___ 
 / __)
( (_ \
 \___/
'''
		
	
class Font:
    def __init__(self, name):
        self.name = name
        self.letters = {}
