from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

Window.size = (280, 530)


class MainScreen(MDScreen, MDApp):
    pass


class Login(MDScreen, MDApp):
    pass


class SignIn(MDScreen):
    pass


class ScreenManger(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark"
        return kv


MyApp().run()
