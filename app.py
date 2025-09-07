from flask import Flask, render_template, request, send_from_directory
import os
from ml_models.analysis import analyze_data

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Welcome Page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Upload Page
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if "file" not in request.files:
            return "No file part", 400
        file = request.files["file"]
        if file.filename == "":
            return "No selected file", 400
        
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        try:
            results, processed_filename = analyze_data(filepath)
        except Exception as e:
            return f"Error analyzing file: {e}", 500

        return render_template(
            "dashboard.html",
            results=results,
            processed_filename=processed_filename
        )
    return render_template("index.html")

# Download processed file
@app.route('/download/<processed_filename>')
def download_file(processed_filename):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        processed_filename,
        as_attachment=True
    )

if __name__ == "__main__":
    # For local dev only
    app.run(host="0.0.0.0", port=5000)
