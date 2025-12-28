from kivy.app import App
from kivy.uix.widget import Widget


class LoginScreen(Widget):
    pass

class FinanseeApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    FinanseeApp().run()