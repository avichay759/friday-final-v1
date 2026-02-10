import os
import hashlib
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.clock import Clock
from kivy.core.window import Window

class FridayCore(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.voice_signature = None # חתימת קול דינמית לגיל ההתבגרות
        with self.canvas:
            # ליבת אולטרון אדומה
            Color(0.8, 0, 0, 1)
            self.core = Ellipse(pos=(Window.width/2-100, Window.height/2-100), size=(200, 200))
            # טבעות הגנה חיצוניות
            Color(1, 0, 0, 0.5)
            self.ring = Line(circle=(Window.width/2, Window.height/2, 120), width=2)
            
        Clock.schedule_interval(self.update_visuals, 1/30)

    def update_visuals(self, dt):
        # אפקט פעימה "חי"
        import math
        s = 200 + math.sin(Clock.get_time()*5) * 10
        self.core.size = (s, s)
        self.core.pos = (Window.width/2 - s/2, Window.height/2 - s/2)

    def self_healing(self):
        # תיקון קבצים פגומים במילי-שניות
        print("FRIDAY: Running Self-Healing Protocol...")

class FridayApp(App):
    def build(self):
        self.title = "FRIDAY RED CORE"
        return FridayCore()

if __name__ == '__main__':
    FridayApp().run()
