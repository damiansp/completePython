from fpdf import FPDF


# To access system fonts:
#fpdf.STYSTEM_TTFONTS = 'path/to/system/fonts'

# or

#import fpdf_mod
#import os

#fpdf_mod.set_global(
#    "SYSTEM_TTFONTS", os.path.join(os.path.dirname(__file__),'fonts'

def change_fonts():
    pdf = FPDF()
    pdf.add_page()
    font_size = 8
    for font in pdf.core_fonts:
        # Skip bold/italicized versions (e.g. helveticaBI)
        if any([letter for letter in font if letter.isupper()]):
            continue
        pdf.set_font(font, size=font_size)
        pdf.set_text_color(0, 64, 128)
        txt = f'{font}: {font_size} pts'
        pdf.cell(0, 10, txt=txt, ln=1, align='C')
        font_size += 2
    pdf.output('change_fonts.pdf')


if __name__ == '__main__':
    change_fonts()
