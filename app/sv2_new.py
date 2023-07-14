import os
import pickle
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, send_file

def init():
    model_path = os.environ.get('MODELPATH')
    if model_path is None:
        model_path = '../model'

    with open(file = os.path.join(model_path, 'service_1.pickle'), mode = 'rb') as f:
        images = pickle.load(f)

    return images

images = init()

def service_2():
    try:
        samples = np.random.randint(len(images), size = 9)
        result = []

        for sample in samples:
            result.append(images[sample])

        plts = []

        plt.figure(figsize = (8, 8))
        for idx, image in enumerate(result):
            plt.subplot(3, 3, idx+1)
            plt.imshow(image, cmap = 'gray')
            plt.axis('off')

            img = BytesIO()
            plt.savefig(img, format = 'png', dpi = 200)
            img.seek(0)
            plts.append(img)

        return len(plts) 
    
    except Exception as e:
        return e, -1



app = Flask(__name__)
app.debug = True

@app.route('/')
def index():

    samples = np.random.randint(len(images), size = 9)
    result = []

    for sample in samples:
        result.append(images[sample])

    plt.figure(figsize = (8, 8))
    for idx, image in enumerate(result):
        plt.subplot(3, 3, idx+1)
        plt.imshow(image, cmap = 'gray')
        plt.axis('off')
    
    img = BytesIO()
    plt.savefig(img, format = 'png', dpi = 200)
    img.seek(0)
    return send_file(img, mimetype = 'image/png')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port = 80)