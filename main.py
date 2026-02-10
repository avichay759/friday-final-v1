from kivy.app import App
from kivy.ux.label import Label
from kivy.ux.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse

class FridayCore(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # כאן אני מזריקה את הליבה האדומה הפועמת בתוך האפליקציה
        with self.canvas:
            Color(1, 0, 0, 1) # אדום
            self.core = Ellipse(pos=(300, 500), size=(200, 200))

class FridayApp(App):
    def build(self):
        return FridayCore()

if __name__ == '__main__':
    FridayApp().run()
