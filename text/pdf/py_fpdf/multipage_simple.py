from fpdf import FPDF


def multipage_simple():
    pdf = FPDF()
    pdf.set_font('Arial', size=12)
    pdf.add_page()
    for i in range(100):
        pdf.cell(0, 10, txt=f'Line # {i:3d}', ln=1)
    pdf.output('multipage_simple.pdf')


if __name__ == '__main__':
    multipage_simple()
