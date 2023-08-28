from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle


class Racket(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def moveRacket(self):
        pass

class PongApp(App):
    
    def build(self):
        root_widget = Racket()
        return root_widget

if __name__ == '__main__':
    PongApp().run()