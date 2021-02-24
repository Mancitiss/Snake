from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy_addons.CustomModules import CustomGraphics
from random import random

#CustomGraphics.SetBG(layout, bg_color=[1,0,0,1])

class snakeApp(App):
	def build(self):
		a = GridLayout(cols = 50)

		list_a = [[GridLayout() for j in range(50)] for i in range(50)]
		for b in list_a:
			for c in b:
				CustomGraphics.SetBG(c, bg_color = [0, 0, 0, 1])
				a.add_widget(c)

		for i in range(3):
			for j in range(3):
				CustomGraphics.SetBG(list_a[i][j], bg_color = [1, 0, 0, 1])
		return a

if __name__ == '__main__':
	snakeApp().run()
