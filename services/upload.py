import os
from flask import request, jsonify, send_file, render_template, after_this_request
from split import allowed_file, generate_zip_file, UPLOAD_FOLDER


def upload_file(app):
    if 'file' not in request.files:
        return render_template("index.html", error="No selected file.")
    file = request.files['file']
    if file.filename == '':
        return render_template("index.html", error="No selected file.")
    if not file or not allowed_file(file.filename):
        return render_template("index.html", error="Invalid file type. Only PDFs are allowed.")

    unique_folder_path, zip_path = generate_zip_file(file)

    @after_this_request
    def remove_file(response):
        try:
            remove_all_files_in_uploads()
        except Exception as e:
            app.logger.error(
                "Error removing or closing downloaded file handle", e)
        return response

    return send_file(zip_path, as_attachment=True)


def remove_all_files_in_uploads():
    for root, dirs, files in os.walk(UPLOAD_FOLDER, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
