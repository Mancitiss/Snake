from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy_addons.CustomModules import CustomGraphics
from kivy.clock import Clock
from functools import partial
from random import random
from kivy.core.window import Window

#CustomGraphics.SetBG(layout, bg_color=[1,0,0,1])

class GameLoop():

	def key_action(self, instance, *args):
		self.text = list(args)[1]
		if (self.text == 273 or self.text == 119):
			instance.direction = 'up'
		elif (self.text == 274 or self.text == 115):
			instance.direction = 'down'
		elif (self.text == 275 or self.text == 100):
			instance.direction = 'right'
		elif (self.text == 276 or self.text == 97):
			instance.direction = 'left'
		print ("got a key event: %s" % self.text)


	def update(self, instance, *args):
		instance.move()
		print(instance.X_pos, ' ', instance.Y_pos)
		

class Snake():
	direction = 'right'
	length = 3
	X_pos = 10
	Y_pos = 10
	def move(self, *args):
		if (self.direction == 'right'):
			self.X_pos += 1
		elif (self.direction == 'left'):
			self.X_pos -= 1
		elif (self.direction == 'up'):
			self.Y_pos -= 1
		elif (self.direction == 'down'):
			self.Y_pos += 1


class snakeApp(App):
	def build(self):
		a = GridLayout(cols = 50)

		list_a = [[GridLayout() for j in range(50)] for i in range(50)]
		for b in list_a:
			for c in b:
				CustomGraphics.SetBG(c, bg_color = [0, 0, 0, 1])
				a.add_widget(c)
		main = Snake()
		g = GameLoop()
		Window.bind(on_key_down = partial(g.key_action, main))
		Clock.schedule_interval(partial(g.update, main), 2)
		
		return a

if __name__ == '__main__':
	snakeApp().run()
