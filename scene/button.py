class Button:
    def __init__(self, position=[], text='', fontSize=30, color=[], func=lambda:None, type='normal'):
        self.position = position
        self.text = text
        self.fontSize = fontSize
        self.color = color
        self.func = func
        self.type = type

    def unpack(self):
        return self.position, self.text, self.fontSize, self.color, self.func