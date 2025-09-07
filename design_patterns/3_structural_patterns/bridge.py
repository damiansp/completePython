def main():
    # client code
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()
    circ1 = Circle(vector_renderer, 5)
    circ2 = Circle(raster_renderer, 3)
    print(circ1.draw())
    print(circ2.draw())
    

# Implementor
class Renderer:
    def render_circle(self, rad):
        pass


# Concrete Implementors
class VectorRenderer(Renderer):
    def render_circle(self, rad):
        return f'Drawing a circle of radius {rad} using vector graphics'


class RasterRenderer(Renderer):
    def render_circle(self, rad):
        return f'Drawing a circle of radius {rad} as pixels'

    


# Abstraction
class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass


# Refined Abstraction
class Circle(Shape):
    def __init__(self, renderer, rad):
        super().__init__(renderer)
        self.rad = rad

    def draw(self):
        return self.renderer.render_circle(self.rad)


if __name__ == '__main__':
    main()
