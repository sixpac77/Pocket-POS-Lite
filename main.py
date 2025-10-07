from kivy.app import App
from kivy.uix.label import Label

class PocketPOSLite(App):
    def build(self):
        return Label(text="Pocket POS Lite ✓", font_size='24sp')

if __name__ == "__main__":
    PocketPOSLite().run()
