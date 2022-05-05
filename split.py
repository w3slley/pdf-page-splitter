import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf(pdf_filename):    
    file_base_name = pdf_filename.replace('.pdf', '')
    output_folder_path = os.path.join(os.getcwd(), 'output')
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)
        
        pdf = PdfFileReader(pdf_filename)

    for page_num in range(pdf.numPages):
        pdfWriter = PdfFileWriter()
        pdfWriter.addPage(pdf.getPage(page_num))

        with open(os.path.join(output_folder_path, 
                           '{0}_Page{1}.pdf'.format(file_base_name, page_num+1)), 'wb') as f:
            pdfWriter.write(f)
            f.close()


if(len(sys.argv) != 2):
    print('Error: please add the pdf filename as an argument')
else:
    pdf_filename = sys.argv[1]
    split_pdf(pdf_filename)
