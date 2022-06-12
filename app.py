import os
import json
import tensorflow as tf
import numpy as np
import tensorflow as keras
import shutil
import time
import pandas as pd
import math

from keras.models import load_model
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['UPLOAD_FOLDER']="images"

model = load_model("model.h5")

# Testing Server
@app.route("/")
def name():
    return 'Fancy Bin'

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == 'POST':
        try:
            shutil.rmtree('images')
        finally:
            os.makedirs('images')
        upload_image=request.files['images']
        filepath=os.path.join(app.config['UPLOAD_FOLDER'],upload_image.filename)
        upload_image.save(filepath)

        #path ke gambar+nama filenya
        fname = "images/{}".format(os.listdir('images/')[0])
        
        image_size = (150, 150)
        test_image = tf.keras.preprocessing.image.load_img(fname, target_size = image_size)
        test_image = tf.keras.preprocessing.image.img_to_array(test_image)*(1/255)
        
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)[0][0] * 100
        anorganic = round(result,2)
        organic = round(100 - result,2)
        display(fname)
        
        if anorganic > 50:
            result = "Anorganic" 
            prediction = str(anorganic) + '% anorganic and ' + str(organic) + "% organic"
        elif anorganic <= 50:
            result = "Organic"
            prediction = str(organic) + '% organic and ' + str(anorganic) + "% anorganic"
      
        return jsonify(result=result, prediction=prediction)
    else:
        return "Internal Server Error, Using Method Get but not run the code"

if __name__ == '__main__':
    app.run(debug=True)
