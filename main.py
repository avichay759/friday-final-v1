import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.clock import Clock
from kivy.core.window import Window

class FridayCore(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # ליבה אדומה סגנון אולטרון
            Color(0.8, 0, 0, 1)
            self.core = Ellipse(pos=(Window.width/2-100, Window.height/2-100), size=(200, 200))
            Color(1, 0, 0, 0.3)
            self.ring = Line(circle=(Window.width/2, Window.height/2, 120), width=3)
            
        Clock.schedule_interval(self.update_visuals, 1/30)

    def update_visuals(self, dt):
        import math
        # פעימת חיים לליבה
        pulse = 200 + math.sin(Clock.get_time()*4) * 15
        self.core.size = (pulse, pulse)
        self.core.pos = (Window.width/2 - pulse/2, Window.height/2 - pulse/2)

class FridayApp(App):
    def build(self):
        return FridayCore()

if __name__ == '__main__':
    # כאן פריידי תבצע סריקת מערכות ראשונית בעליה
    FridayApp().run()
