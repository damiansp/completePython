import os
from fpdf import FPDF

HOME = os.environ['HOME']
URL = ('http://www.blog.pythonlibrary.org/wp-content/uploads/2018/06/'
       'add_image-243x300.png')

def add_image(path):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(path, x=10, y=8, w=100)
    pdf.set_font('Arial', size=12)
    pdf.ln(85) # move 85 down
    pdf.cell(20, 10, txt=path, ln=1)
    # Synax not correct:
    #pdf.image('snakehead', x=10, y=200, w=50, type='jpg', link=URL)
    pdf.output('add_image.pdf')


if __name__ == '__main__':
    add_image(f'{HOME}/Desktop/images/beards.png')
