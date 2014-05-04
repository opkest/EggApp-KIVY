import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class EggCook(BoxLayout):
    def button1(self, *args):
        Clock.schedule_once(self.alarm, 5)

    def button2(self, *args):
        Clock.schedule_once(self.alarm, 600)

    def alarm(self, *args):
        sound = SoundLoader.load('audio/chicken.wav')
        popup = Popup(title = 'Attention!',
                      content = Label(text = 'Egg is boiled!'),
                      size_hint = (None, None),
                      size = (300, 300))
        popup.open()
        sound.play()


class EggCookApp(App):
    def build(self):
        return EggCook()


if __name__ == '__main__':
    EggCookApp().run()
