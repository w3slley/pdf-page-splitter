from flask import Flask, render_template
from services.upload import upload_file

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(413)
def request_entity_too_large(error):
    return render_template("partials/error.html", error="<p>File too large. Maximum file size is 10 MB."), 413


@app.route('/upload', methods=['POST'])
def upload():
    return upload_file(app)
