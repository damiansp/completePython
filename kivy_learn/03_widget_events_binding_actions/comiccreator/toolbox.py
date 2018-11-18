import math

import kivy
from kivy.graphics import Line
from kivy.uix.togglebutton import ToggleButton

from comicwidgets import StickMan, DraggableWidget

kivy.require('1.9.0')


class ToolButton(ToggleButton):
    def on_touch_down(self, touch):
        ds = self.parent.drawing_space
        if self.state == 'down' and ds.collide_point(touch.x, touch.y):
            x, y = ds.to_widget(touch.x, touch.y)
            self.draw(ds, x, y)
            return True
        retrun super(ToolButton, self).on_touch_down(touch)

    def draw(self, ds, x, y):
        pass

