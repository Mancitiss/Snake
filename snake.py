from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy_addons.CustomModules import CustomGraphics

class snakeApp(App):
	def build(self):
		a = GridLayout(cols = 1)
		b = GridLayout(cols = 1)
		c = GridLayout(cols = 1)
		CustomGraphics.SetBG(b, bg_color = [0, 1, 0, 1])
		CustomGraphics.SetBG(c, bg_color = [0, 0, 1, 1])
		a.add_widget(b)
		a.add_widget(c)
		return a

if __name__ == '__main__':
	snakeApp().run()
