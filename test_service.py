import os
import pickle
import numpy as np
from flask import Flask, send_file

model_path = os.environ.get('MODELPATH')
if model_path is None:
    model_path = 'model'

with open(file = os.path.join(model_path, 'service_1.pickle'), mode = 'rb') as f:
    images = pickle.load(f)

def test_image():
    image = images[0]
    assert image.shape == (224, 224)
