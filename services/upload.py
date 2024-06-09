import os
from flask import request, jsonify, send_file, render_template, after_this_request
from split import allowed_file, generate_zip_file


def upload_file(app):
    if 'file' not in request.files:
        return render_template("partials/error.html", error="No selected file."), 400
    file = request.files['file']
    if file.filename == '':
        return render_template("partials/error.html", error="No selected file."), 400
    if not file or not allowed_file(file.filename):
        return render_template("partials/error.html", error="Invalid file type. Only PDFs are allowed."), 400

    unique_folder_path, zip_path = generate_zip_file(file)

    @after_this_request
    def remove_file(response):
        try:
            remove_all_files(unique_folder_path)
            os.rmdir(unique_folder_path)
        except Exception as e:
            app.logger.error(
                "Error removing or closing downloaded file handle", e)

        return render_template('partials/error.html', error="Internal server error. Please try again later."), 500

    return send_file(zip_path, as_attachment=True)


def remove_all_files(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for f in files:
            os.remove(os.path.join(root, f))
