import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.9.0')

class MyFirstApplication(App):

    def build(self):
        return Label(text='This is my first App!!')

if __name__ == '__main__':
    MyFirstApplication().run()