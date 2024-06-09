import os
import zipfile
import uuid
from PyPDF2 import PdfReader, PdfWriter
from werkzeug.utils import secure_filename

output_folder_path_cli = os.path.join(os.getcwd(), 'output')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = ['pdf']


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def split_pdf(pdf_filename, save_folder=output_folder_path_cli):
    pdf = PdfReader(os.path.join(save_folder, pdf_filename))
    pdf_page_size = len(pdf.pages)
    for page_num in range(pdf_page_size):
        pdfWriter = PdfWriter()
        pdfWriter.add_page(pdf.pages[page_num])
        output_file = '{0}/{1}.pdf'.format(save_folder, page_num+1)
        with open(os.path.join(output_file), 'wb') as f:
            pdfWriter.write(f)
            f.close()
    return pdf_page_size


def generate_zip_file(file):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    filename = secure_filename(file.filename)
    unique_uuid = str(uuid.uuid4())
    unique_folder_path = os.path.join(
        UPLOAD_FOLDER, unique_uuid)
    os.makedirs(unique_folder_path)
    file.save(os.path.join(unique_folder_path, filename))
    pages_num = split_pdf(filename, unique_folder_path)
    zip_path = os.path.join(
        unique_folder_path, f"{filename}.zip"
    )
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for i in range(1, pages_num+1):
            split_filename = str(i) + '.pdf'
            zipf.write(
                os.path.join(unique_folder_path, split_filename), arcname=split_filename
            )
    return unique_folder_path, zip_path
