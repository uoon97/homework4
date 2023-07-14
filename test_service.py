import os
import pickle
import numpy as np

model_path = os.environ.get('MODELPATH')
if model_path is None:
    model_path = 'model'

with open(file = os.path.join(model_path, 'service_1.pickle'), mode = 'rb') as f:
    images = np.array(pickle.load(f))

def test_image():
    image = images[0]
    assert image.shape == (224, 224)
