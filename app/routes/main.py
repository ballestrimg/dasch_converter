from ..app import app, ALLOWED_EXTENSIONS
import os
from io import BytesIO
import numpy as np 

from flask import render_template, redirect, request, url_for, send_file, send_from_directory 
from werkzeug.utils import secure_filename
from PIL import Image

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def resize_image(filename, max_width=1024, max_height=1024):
    img = Image.open(filename)
    width, height = img.size

    if width > max_width or height > max_height:
        ratio = min(max_width / width, max_height / height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)

        # redefine 'img' variable
        img = img.resize((new_width, new_height), Image.LANCZOS)

    return img # CODE OK

@app.route("/") # TALVEZ ADD methods=['GET', 'POST']
def home():
    return render_template("pages/main.html")

@app.route("/convert", methods=['POST']) # TALVEZ ADD GET AS METHOD
def upload_image():

    if 'file' not in request.files:
        return redirect(request.url) # ver o que significa var request.url
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url) # ver o que significa var request.url

    '''aparentemente até aqui tá tudo certo, verificar apenas o que é request.url'''

    if file and allowed_file(file.filename): # até aqui ta OK
        filename = secure_filename(file.filename) # not used yet
        # HYPOTHESIS USING BO INSTEAD RESIZE FILE
        resized_image = resize_image(file)
        img_io = BytesIO()
        resized_image.save(img_io, 'JPEG')
        img_io.seek(0)
    
        # return send_file(img_io, as_attachment=True)
        return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name= 'resized_file.jpeg')
    
    return redirect(url_for(home))

@app.route("/error")
def error_404():
    return render_template("errors/404.html")

@app.route("/error_500")
def error_500():
    return render_template("errors/500.html")

# TEST CASES
@app.route("/load")
def load():
    return render_template("pages_test/load.html")

@app.route("/load_new")
def load4():
    return render_template("pages_test/hover.html")