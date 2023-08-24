from libs import *
def Instance(self):
    Menu = Scene('assets/bg-1.jpg', 'Menu')
    Menu.fields.append(Element((WIN_CENTER[0]-LABEL_FONT_SIZE, 90), (255, 255, 255), is_text=True, text='Меню', bold=True, fontSize=LABEL_FONT_SIZE))
    Menu.buttons.append(pack(DEFAULT_BUTTON_RES, 'Старт', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR, lambda: self.changeScene('MC1')))
    Menu.buttons.append(pack(DEFAULT_BUTTON_RES, 'Настройки', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR, lambda: print('button')))
    Menu.buttons.append(pack(type='empty'))
    Menu.buttons.append(pack(DEFAULT_BUTTON_RES, 'Выход', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR, lambda: sys.exit()))
    self.addScene(Menu)

    MC1 = Scene('assets/mc_donalds-forest.jpg', 'MC1')
    MC1.buttons.append(pack(DEFAULT_BUTTON_RES, 'Пойти в Макдональдс', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR, lambda: print('goto')))
    MC1.buttons.append(pack(DEFAULT_BUTTON_RES, 'Уйти проч', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR, lambda: self.changeScene('Pene')))
    MC1.buttons.append(pack(DEFAULT_BUTTON_RES, 'Вернуться в меню', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR,lambda: self.changeScene('Menu')))
    self.addScene(MC1)

    Pene = Scene('assets/pene_normal.jpg', 'Pene')
    Pene.buttons.append(pack(DEFAULT_BUTTON_RES, 'Осмотреть', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR, lambda: self.changeScene('P_Pene')))
    Pene.buttons.append(pack(DEFAULT_BUTTON_RES, 'Уйти проч', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR, lambda: self.monologue('Ты долго ходил по лесу, и в итоге умер от голода и жажды...')))
    self.addScene(Pene)

    P_Pene = Scene('assets/p_on_pene.jpg', 'P_Pene')
    self.addScene(P_Pene)

    Test = Scene('assets/pene.jpg', 'Test')
    Test.fields.append(Element((WIN_CENTER[0]-LABEL_FONT_SIZE, 90), (0, 0, 0), is_text=True, text='Пасхалка!', bold=True, fontSize=LABEL_FONT_SIZE))
    Test.buttons.append(pack(DEFAULT_BUTTON_RES, 'Change Scene', DEFAULT_BUTTON_FONTSIZE, DEFAULT_BUTTON_COLOR, lambda: self.changeScene('Menu')))
    self.addScene(Test)