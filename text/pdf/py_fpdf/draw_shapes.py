from fpdf import FPDF


def draw_shapes():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(0, 255, 255)
    pdf.ellipse(10, 10, 10, 100, 'F') # F: Fill; DF: Draw & fill

    pdf.set_line_width(1)
    pdf.set_fill_color(255, 0, 255)
    pdf.rect(15, 15, 100, 50)
    pdf.output('draw_shapes.pdf')


if __name__ == '__main__':
    draw_shapes()
