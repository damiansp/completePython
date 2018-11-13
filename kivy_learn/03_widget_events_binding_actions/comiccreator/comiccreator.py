from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout


for f in ['toolbox.kv', 'drawingspace.kv', 'generaloptions.kv', 'statusbar.kv',
          'comicwidgets.kv']:
    Builder.load_file(f)


class ComicCreator(AnchorLayout):
    pass


class ComicCreatorApp(App):
    def build(self):
        return ComicCreator()



if __name__ == '__main__':
    ComicCreatorApp().run()
