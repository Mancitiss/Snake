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
		if (self.text == 273 or self.text == 119) and (instance.direction != 'down'):
			instance.direction = 'up'
		elif (self.text == 274 or self.text == 115) and ((instance.direction != 'up')):
			instance.direction = 'down'
		elif (self.text == 275 or self.text == 100) and (instance.direction != 'left'):
			instance.direction = 'right'
		elif (self.text == 276 or self.text == 97) and (instance.direction != 'right'):
			instance.direction = 'left'
		print ("got a key event: %s" % self.text)


	def update(self, instance, grid_list, *args):
		instance.move()
		print(instance.X_pos, ' ', instance.Y_pos)
		CustomGraphics.SetBG(grid_list[instance.Y_pos][instance.X_pos], bg_color = [0, 1, 0, 1])
		CustomGraphics.SetBG(grid_list[instance.draw[1][1]][instance.draw[1][0]], bg_color = [1, 0, 0, 1])
		CustomGraphics.SetBG(grid_list[instance.draw[-1][1]][instance.draw[-1][0]], bg_color = [0, 0, 0, 1])
		

class Snake():

	def __init__(self, X_pos = 10, Y_pos = 10, length = 3, direction = 'right'):
		self.X_pos = X_pos
		self.Y_pos = Y_pos
		self.length = length
		self.direction = direction
		self.draw = [(self.X_pos, self.Y_pos) for _ in range(self.length+1)]
		if (self.direction == 'right'):
			for i in range(1, len(self.draw)):
				self.draw[i] = ((self.draw[i][0] - i) % 50, self.draw[i][1] )
		elif (self.direction == 'left'):
			for i in range(1, len(self.draw)):
				self.draw[i] = ((self.draw[i][0] + i) % 50, self.draw[i][1] )
		elif (self.direction == 'up'):
			for i in range(1, len(self.draw)):
				self.draw[i] = (self.draw[i][0] , (self.draw[i][1] + i) % 50)
		elif (self.direction == 'down'):
			for i in range(1, len(self.draw)):
				self.draw[i] = (self.draw[i][0] , (self.draw[i][1] - i) % 50)

	def move(self, *args):
		self.draw[1:] = self.draw[:-1]
		if (self.direction == 'right'):
			self.X_pos = (self.X_pos + 1) % 50
		elif (self.direction == 'left'):
			self.X_pos = (self.X_pos - 1) % 50
		elif (self.direction == 'up'):
			self.Y_pos = (self.Y_pos - 1) % 50
		elif (self.direction == 'down'):
			self.Y_pos = (self.Y_pos + 1) % 50
		self.draw[0] = (self.X_pos, self.Y_pos)


class snakeApp(App):
	def build(self):
		main = Snake(X_pos = 20, Y_pos = 20)
		grid = GridLayout(cols = 50)

		list_a = [[GridLayout() for j in range(50)] for i in range(50)]
		for b in list_a:
			for c in b:
				CustomGraphics.SetBG(c, bg_color = [0, 0, 0, 1])
				grid.add_widget(c)

		CustomGraphics.SetBG(list_a[main.Y_pos][main.X_pos], bg_color = [0, 1, 0, 1])
		for i in range(1, len(main.draw) -1):
			CustomGraphics.SetBG(list_a[main.draw[i][1]][main.draw[i][0]], bg_color = [1, 0, 0, 1])

		g = GameLoop()
		Window.bind(on_key_down = partial(g.key_action, main))
		Clock.schedule_interval(partial(g.update, main, list_a), 0)
		
		return grid

if __name__ == '__main__':
	snakeApp().run()
