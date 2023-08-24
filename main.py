from libs import *

class Game:
	def __init__(self):
		pg.init()
		pg.display.set_caption('game')
		self.clock = pg.time.Clock()
		self.app = pg.display.set_mode(WIN_RES)
		self.placer = Placer(self.app)
		self.buttons = []
		self.localScene = 'Menu'
		self.scenes = []
		self.on_init()

	def newButton(self, RES, text, fontSize, COLOR, func=lambda:None):
		multiplier = len(self.buttons)
		H_POS = RES[1]
		H_RES = RES[3]
		if multiplier > 0: H_POS += (H_RES+SPACE) * multiplier
		button = Button(self.app,
						x=RES[0],
						y=H_POS,
						width=RES[2],
						height=H_RES,
						text=text,
						fontSize=fontSize,
						inactiveColour=COLOR[0],
						hoverColour=COLOR[1],
						pressedColour=COLOR[2],
						onClick=lambda: func())
		self.buttons.append(button)
	def emptyButton(self): return None

	def clean(self):
		for button in self.buttons:
			if not button == None:
				button.hide()
		self.buttons = []
		self.app.fill((0, 0, 0))

	def addScene(self, scene: Scene): self.scenes.append(scene)

	def nextScene(self):
		lScene = Scene
		for scene in self.scenes:
			if scene.name == self.localScene:
				lScene = scene
		nextIndex = self.scenes.index(lScene) + 1
		if nextIndex > len(self.scenes) - 1:
			nextIndex = 0
		self.localScene = self.scenes[nextIndex].name
		self.build()

	def changeScene(self, name):
		targetScene = None
		for scene in self.scenes:
			if scene.name == name:
				targetScene = scene
		self.localScene = targetScene.name
		self.build()

	def on_init(self):
		# Create a scenes instances
		Instance(self)

	def build(self):
		# Clear buttons
		self.clean()
		# Build local scene
		lScene = Scene('','')
		for scene in self.scenes:
			if scene.name == self.localScene:
				lScene = scene
		self.placer.bg(lScene.bg)
		for field in lScene.fields:
			self.placer.place(field)
		for button in lScene.buttons:
			if not button.type == 'empty':
				pos, text, fontsize, color, func = button.unpack()
				#self.buttons.append(self.newButton(pos, text, fontsize, color, func))
				self.newButton(pos, text, fontsize, color, func)
			else:
				self.buttons.append(self.emptyButton())


	def run(self):
		app = self.app
		while True:
			events = pg.event.get()
			for event in events:
				if event.type == pg.QUIT:
					sys.exit()
				if event.type == pg.KEYDOWN and event.key == pg.K_UP:
					self.nextScene()
			pg.display.flip()
			pw.update(events)
			self.clock.tick(30)

if __name__ == '__main__':
	game = Game()
	game.build()
	game.run()
