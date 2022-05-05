import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf(pdf_filename):
    if(len(sys.argv) != 2):
        return print('Please add the pdf filename as an argument')
    
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

pdf_filename = sys.argv[1]
split_pdf(pdf_filename)
