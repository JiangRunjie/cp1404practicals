from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

COLOR: (1,0.6,0.6,1)


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (1,1,1,0)
        self.names = ["Bob", "Peter", "James", "Helen", "Roby"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)
            
    def change_color(self):
        self.background_color = COLOR


DynamicLabelsApp().run()
