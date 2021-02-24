from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class snakeApp(App):
	def build(self):
		a = GridLayout()
		return a

if __name__ == '__main__':
	snakeApp().run()
