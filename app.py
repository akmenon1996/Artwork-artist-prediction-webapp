import os
from flask import Flask, flash, request, redirect, url_for, jsonify,render_template
from werkzeug.utils import secure_filename
import cv2
from tensorflow import keras
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
import pickle
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import os, os.path
import base64
import webbrowser



UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image = cv2.imread(os.path.dirname(os.path.realpath(__file__)) + "/uploads/" + filename)
            color_result = getDominantColor(image)
            img,artist,perc = artist_predict(image)
            print(img)
            redirect(url_for('upload_file', filename=filename))

            return render_template('predict.html',returned_image = img,
                                   color_result=color_result,
                                   artist = artist,
                                   perc = perc
                                   )

    return render_template("home.html")


def artist_predict(uploaded_image):
    image_val = uploaded_image
    train_input_shape = (224, 224, 3)
    model = load_model('models/trained_model.hdf5')
    with open('models/labels.pickle', 'rb') as handle:
      labels = pickle.load(handle)
    uploaded_image = cv2.resize(uploaded_image, dsize=train_input_shape[0:2], )
    uploaded_image = keras.preprocessing.image.img_to_array(uploaded_image)
    uploaded_image /= 255.
    uploaded_image = np.expand_dims(uploaded_image,axis=0)
    prediction = model.predict(uploaded_image)
    prediction_probability = np.amax(prediction)
    prediction_idx = np.argmax(prediction)
    artist = labels[prediction_idx].replace('_', ' ')
    probability_perc = str(prediction_probability * 100)
    print("Predicted artist =", labels[prediction_idx].replace('_', ' '))
    print("Prediction probability =", prediction_probability * 100, "%")
    title = "Predicted artist = {}\nPrediction probability = {:.2f} %" \
        .format(labels[prediction_idx].replace('_', ' '),
                prediction_probability * 100)
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title(title)
    axis.imshow(image_val[...,::-1])

    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')


    K.clear_session()

    return (pngImageB64String,artist,probability_perc)


@app.route('/about')
def my_page():
    return webbrowser.open_new_tab('https://github.com/akmenon1996/Artwork-artist-prediction-webapp/blob/master/README.md')

def getDominantColor(image):
    '''returns the dominate color among Blue, Green and Reds in the image '''
    B, G, R = cv2.split(image)
    B, G, R = np.sum(B), np.sum(G), np.sum(R)
    color_sums = [B, G, R]
    color_values = {"0": "Blue", "1": "Green", "2": "Red"}
    return color_values[str(np.argmax(color_sums))]



if __name__ == "__main__":
    app.run(debug=False)