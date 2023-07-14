import os
import pickle
import numpy as np
from PIL import Image

def service_1():
    image_path = os.environ.get('IMAGEPATH')
    if image_path is None:
        image_path = '../data'

    def load_data():

        numbers = range(0, 10)
        images = []

        for n in numbers:
            globals()[f'fname_{n}'] = os.listdir(os.path.join(image_path, f'{n}'))

        for n in numbers:
                for i in range(len(globals()[f'fname_{n}'])):
                    f = os.path.join(image_path, f'{n}', globals()[f'fname_{n}'][i])
                    image = Image.open(f)
                    image = image.resize((224, 224))
                    arr = np.array(image)
                    images.append(arr)

        return images

    images = load_data()

    return len(images)


if __name__ == "__main__":
    service_1()