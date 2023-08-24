from libs import *

class Placer:
    def __init__(self, app: pg.display):
        self.app = app

    def place(self, element):
        if not element.is_text:
            if element.image == '':
                pg.draw.rect(self.app, color=element.color, rect=element.position)
            else:
                texture = pg.image.load(element.image)
                self.app.blit(texture, element.position)
        if element.is_text:
            f1 = pg.font.SysFont(None, element.fontSize)
            text = f1.render(element.text, element.bold, element.color)
            self.app.blit(text, element.position)

    def bg(self, texPath: str()):
        bgTex = pg.image.load(texPath)
        self.app.blit(bgTex, (0, 0))
