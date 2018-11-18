import math

import kivy
from kivy.graphics import Line
from kivy.uix.togglebutton import ToggleButton

from comicwidgets import StickMan, DraggableWidget

kivy.require('1.9.0')


class ToolButton(ToggleButton):
    def on_touch_down(self, touch):
        drawing_space = self.parent.drawing_space
        if self.state == 'down' and drawing_space.collide_point(touch.x,
                                                                touch.y):
            x, y = drawing_space.to_widget(touch.x, touch.y)
            self.draw(drawing_space, x, y)
            return True
        return super(ToolButton, self).on_touch_down(touch)

    def draw(self, drawing_space, x, y):
        stick_man = StickMan(width=48, height=48)
        stick_man.center = (x, y)
        drawing_space.add_widget(stick_man)


        
class ToolFigure(ToolButton):
    def draw(self, drawing_space, x, y):
        self.ix, self.iy = x, y
        with drawing_space.canvas:
            self.figure = self.create_figure(x, y, x + 1, y + 1)
        drawing_space.bind(on_touch_move=self.update_figure)
        drawing_space.bind(on_touch_up=self.end_figure)
