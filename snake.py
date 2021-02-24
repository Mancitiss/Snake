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
		
		list_a = [GridLayout() for _ in range(2500)]
		for c in list_a:
			CustomGraphics.SetBG(c, bg_color = [random(), random(), random(), 1])
			a.add_widget(c)
		return a

if __name__ == '__main__':
	snakeApp().run()
