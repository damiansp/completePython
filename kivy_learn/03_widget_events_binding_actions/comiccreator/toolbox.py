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
        pass



class ToolStickman(ToolButton):
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

    def update_figure(self, drawing_space, touch):
        if drawing_space.collide_point(touch.x, touch.y):
            x, y = drawing_space.to_widget(touch.x, touch.y)
            drawing_space.canvas.remove(self.figure)
            with drawing_space.canvas:
                self.figure = self.create_figure(self.ix, self.iy, x, y)

    def end_figure(self, drawing_space, touch):
        drawing_space.unbind(on_touch_move=self.update_figure)
        drawing_space.unbind(on_touch_up=self.end_figure)
        drawing_space.canvas.remove(self.figure)
        fx, fy = drawing_space.to_widget(touch.x, touch.y)
        self.widgetise(drawing_space, self.ix, self.iy, fx, fy)

    def widgetise(self, drawing_space, ix, iy, fx, fy):
        widget = self.create_widget(ix, iy, fx, fy)
        ix, iy = widget.to_local(ix, iy, relative=True)
        fx, fy = widget.to_local(fx, fy, relative=True)
        widget.canvas.add(self.create_figure(ix, iy, fx, fy))
        drawing_space.add_widget(widget)

    def create_figure(self, ix, iy, fx, fy):
        pass

    def create_widget(self, ix, iy, fx, fy):
        pass



class ToolLine(ToolFigure):
    def create_figure(self, ix, iy, fx,fy):
        return Line(points=[ix, iy, fx, fy])

    def create_wiget(self, ix, iy, fx, fy):
        pos = (min(ix, fx), min(iy, fy))
        size = (abs(fx - ix), abs(fy - iy))
        return DraggableWidget(pos=pos, size=size)



class ToolCircle(ToolFigure):
    def create_figure(self, ix, iy, fx, fy):
        return Line(circle=[ix, iy, math.hypot(ix - fx, iy - fy)])

    def create_widget(self, ix, iy, fx, fy):
        r = math.hypot(ix - fx, iy - fy)
        pos = (ix - r, iy - r)
        size = (2*r, 2*r)
        return DraggableWidget(pos=pos, size=size)
