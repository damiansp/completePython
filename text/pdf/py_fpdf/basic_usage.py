from fpdf import FPDF


#pdf = FPDF() # defaults to:
pdf = FPDF(orientation='P', unit='mm', format='A4') # L for landscape
pdf.add_page()
pdf.set_font('Arial', size=12)
# ln=1 means terminate line with \n
pdf.cell(200, 10, txt='Welcome to PyFpdf!', ln=1, align='C')
pdf.output('basic_usage.pdf')
