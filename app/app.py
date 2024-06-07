import os
from flask import Flask, request, redirect, render_template, send_from_directory

from cyclegan import convert_image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads/"
MODELS_FOLDER = "static/models/"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MODELS_FOLDER"] = MODELS_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    models = os.listdir(app.config["MODELS_FOLDER"])
    return render_template("index.html", models=models)


@app.route("/upload", methods=["POST"])
def upload_file():
    # Check if a file was submitted
    if "file" not in request.files:
        return redirect(request.url)
    file = request.files["file"]
    # If no file was submitted
    if file.filename == "":
        return redirect(request.url)
    # If the file is valid
    if file and allowed_file(file.filename):
        # Clear the uploads folder
        for f in os.listdir(app.config["UPLOAD_FOLDER"]):
            os.remove(os.path.join(app.config["UPLOAD_FOLDER"], f))

        filename = file.filename
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)  # type: ignore
        file.save(filepath)

        preprocessing = request.form.get('preprocess')
        load_size = request.form.get('load_size')
        crop_size = request.form.get('crop_size')
        width = request.form.get('width')

        options = {"preprocess": preprocessing, "load_size": load_size, "crop_size": crop_size, "width": width}

        # Get the folder where the image is saved
        folder = os.path.dirname(os.path.abspath(filepath))

        model = request.form.get("model")
        # Convert the image using CycleGAN model
        converted_image_path = convert_image(folder, options, model)

        return render_template("result.html", original_image=filename, converted_image=converted_image_path)

    return redirect(request.url)


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    if not os.path.exists("../training"):
        raise Exception("The training folder does not exist. Please check installation instructions.")
    if not os.path.exists("../training/checkpoints/pixelart/"):
        os.makedirs("../training/checkpoints/pixelart/")
    if not os.path.exists("../training/results/pixelart/test_latest/images/"):
        os.makedirs("../training/results/pixelart/test_latest/images/")
    app.run(debug=True)
