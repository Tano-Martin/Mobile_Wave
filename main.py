from kivymd.app import MDApp
from kivy.config import Config
from kivy.uix import screenmanager


class WaveApp(MDApp):
    pass


class Navigation(screenmanager.ScreenManager):
    list_page = []

    def go_to(self, name):
        if name not in self.list_page:
            self.list_page.append(self.current)

            self.transition.direction = "left"
            self.current = name


    def back(self):
        if len(self.list_page) > 0:
            name = self.list_page[-1]
            del self.list_page[-1]

            self.transition.direction = "right"
            self.current = name


# Config.set("graphics", "width", "420")
# Config.set("graphics", "height", "650")
# Config.set("graphics", "resizable", "0")

WaveApp().run()
