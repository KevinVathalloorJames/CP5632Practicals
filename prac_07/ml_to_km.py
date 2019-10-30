from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
MILE_KM = 1.60934


class MileConverter(App):

    def build(self):
        Window.size = (500, 500)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('m_km.kv')
        return self.root

    def get_miles(self):
        try:
            mile_value = float(self.root.ids.miles.text)
            return mile_value
        except ValueError:
            return 0

    def handle_calculate(self):
        mile_value = self.get_miles()
        km_value = mile_value * MILE_KM
        self.root.ids.output_label.text = str(km_value)

    def handle_increment(self, increment_value):
        mile_value = self.get_miles() + increment_value
        self.root.ids.miles.text = str(mile_value)
        self.handle_calculate()


MileConverter().run()
