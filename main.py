import requests
from kivy.app import App
from kivy.uix.button import Button

class FridayApp(App):
    def build(self):
        # הממשק האדום שלך
        btn = Button(text='INITIALIZE FRIDAY VOICE', 
                     background_color=(1, 0, 0, 1),
                     font_size=25)
        btn.bind(on_press=self.activate_voice)
        return btn

    def activate_voice(self, instance):
        print("Connecting to Neural Voice Engine...")
        # כאן אני מזריקה את החיבור ל-ElevenLabs בשלב הבא
        instance.text = "VOICE ENGINE READY"

if __name__ == '__main__':
    FridayApp().run()
