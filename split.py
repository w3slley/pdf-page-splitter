import os
import sys
from PyPDF2 import PdfReader, PdfWriter

output_folder_path = os.path.join(os.getcwd(), 'output')

def split_pdf(pdf_filename):
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)
    pdf = PdfReader(pdf_filename)
    for page_num in range(len(pdf.pages)):
        pdfWriter = PdfWriter()
        pdfWriter.add_page(pdf.pages[page_num])
        with open(os.path.join(output_folder_path, '{0}/page-{1}.pdf'.format(output_folder_path, page_num+1)), 'wb') as f:
            pdfWriter.write(f)
            f.close()

if (len(sys.argv) < 2):
    print('Error: please add the pdf filename as an argument')
else:
    pdf_filename = sys.argv[1]
    split_pdf(pdf_filename)
