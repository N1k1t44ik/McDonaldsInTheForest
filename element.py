
class Vector2:
	def __init__(self, x=0,  y=0):
		self.x = x
		self.y = y
class Vector3:
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

class Element:
	def __init__(self, position, color=Vector3(0, 0, 0), image='', is_text=False, bold=False, text='', fontSize=30):
		self.position = position
		self.color = color
		self.image = image
		self.is_text = is_text
		self.text = text
		self.bold = bold
		self.fontSize = fontSize

	def drop(self):
		self.position = [Vector2(0, 0), Vector2(0, 0)]
		self.color = Vector3(0, 0, 0)
		self.image = ''
		self.is_text = False
		self.text = ''
