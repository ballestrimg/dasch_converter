from ..app import app, ALLOWED_EXTENSIONS
from io import BytesIO
 
from flask import render_template, redirect, request, url_for, send_file
from werkzeug.utils import secure_filename
from PIL import Image

# set global variable : None == no limits to pixels
Image.MAX_IMAGE_PIXELS = None

# function allowed_files : define extensions allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# function resize_images : define 1024x1024 pixels to output files
def resize_image(filename, max_width=1024, max_height=1024):
    img = Image.open(filename)
    width, height = img.size

    if width > max_width or height > max_height:
        ratio = min(max_width / width, max_height / height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)

        # redefine 'img' variable
        img = img.resize((new_width, new_height), Image.LANCZOS)

    return img

# route home
@app.route("/")
def home():
    return render_template("pages/main.html")

# route convert
@app.route("/convert", methods=['POST'])

# function upload image : check file extension, save it to BytesIO and apply new filename
def upload_image():

    if 'file' not in request.files:
        return redirect(request.url) 
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url) 

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_extension = filename.rsplit('.', 1)[1].lower()
        
        resized_image = resize_image(file)
        img_io = BytesIO()
        
        if file_extension == 'jpeg' or file_extension == 'jpg':
            resized_image.save(img_io, 'JPEG')
            mimetype = 'image/jpeg'
            download_name = f'{filename.rsplit('.', 1)[1]}_resized.jpeg'
        elif file_extension == 'png':
            resized_image.save(img_io, 'PNG')
            mimetype = 'image/png'
            download_name = f'{filename.rsplit('.', 1)[1]}_resized.jpeg'

        img_io.seek(0)
    
        return send_file(img_io, mimetype=mimetype, as_attachment=True, download_name=download_name)
    
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
