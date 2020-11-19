# a working prototype has been finally created !

from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("design.kv")


class ScreenOne(Screen):
    python_name = ObjectProperty(None)
    python_domain = ObjectProperty(None)
    python_major = ObjectProperty(None)

    def but_prs(self):
        global global_name
        global global_domain
        global global_major
        global_name = str(self.python_name.text)
        global_domain = str(self.python_domain.text)
        global_major = str(self.python_major.text)

    @property
    def clear_screen(self):
        self.python_name.text = ""
        self.python_domain.text = ""
        self.python_major.text = ""


class ScreenTwo(Screen):
    python_input = ObjectProperty(None)

    @property
    def clr_scrn(self):
        self.python_input.text = ""

    def button_pressed(self):
        if global_name != "" and global_domain != "" and global_major != "":
            self.python_input.text = "your name is {}; your domain is {} and your major is {}".format(
                global_name, global_domain, global_major)


class Manager(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)


class MainApp(App):
    def build(self):
        return Manager()


if __name__ == '__main__':
    MainApp().run()
