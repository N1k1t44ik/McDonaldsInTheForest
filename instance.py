from libs import *
def Instance(self):
    Menu = Scene('assets/bg-1.jpg', 'Menu')
    Menu.fields.append(Element((WIN_CENTER[0]-LABEL_FONT_SIZE, 90), (255, 255, 255), is_text=True, text='Menu', bold=True, fontSize=LABEL_FONT_SIZE))
    Menu.buttons.append(pack(DEFAULT_BUTTON_RES, 'start', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR, lambda: self.changeScene('MC1')))
    Menu.buttons.append(pack(DEFAULT_BUTTON_RES, 'settings', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR, lambda: print('button')))
    Menu.buttons.append(pack(type='empty'))
    Menu.buttons.append(pack(DEFAULT_BUTTON_RES, 'exit', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR, lambda: sys.exit()))
    self.addScene(Menu)

    MC1 = Scene('assets/mc_donalds-forest.jpg', 'MC1')
    MC1.buttons.append(pack(DEFAULT_BUTTON_RES, 'Go to McDonalds', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR, lambda: print('goto')))
    MC1.buttons.append(pack(DEFAULT_BUTTON_RES, 'To Menu', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR,lambda: self.changeScene('Menu')))
    self.addScene(MC1)

    Test = Scene('assets/pene.jpg', 'Test')
    Test.fields.append(Element((WIN_CENTER[0]-LABEL_FONT_SIZE, 90), (0, 0, 0), is_text=True, text='Test', bold=True, fontSize=LABEL_FONT_SIZE))
    Test.buttons.append(pack(DEFAULT_BUTTON_RES, 'Change Scene', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR, lambda: self.changeScene('Menu')))
    self.addScene(Test)