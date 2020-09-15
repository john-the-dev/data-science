from PIL import Image
from PIL import ImageFilter
from os import path

class EmbossError(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else ''
supportedExtensions = set(['.jpg', '.png'])
class Emboss:
    def __init__(self, imagePath):
        if not path.exists(imagePath): raise EmbossError('Image file not found: {}'.format(imagePath))
        k = imagePath.rfind('.')
        if k < 0 or imagePath[k:].lower() not in supportedExtensions: raise EmbossError('Image file type not supported. Supported types include {}'.format(supportedExtensions))
        self.imagePath = imagePath
        
    def showOriginal(self):
        Image.open(self.imagePath).show()

    def showEmboss(self):
        Image.open(self.imagePath).filter(ImageFilter.EMBOSS).show()

    def save(self):
        k = self.imagePath.rfind('.')
        embossPath = '{}_emboss{}'.format(self.imagePath[:k],self.imagePath[k:])
        Image.open(self.imagePath).filter(ImageFilter.EMBOSS).save(embossPath)
        print('Emboss image saved to {}'.format(embossPath))