from deepface.basemodels import Facenet
from pathlib import Path
import os
import gdown

from deepface.commons import functions

def loadModel(url = 'https://github.com/serengil/deepface_models/releases/download/v1.0/facenet512_weights.h5'):

    model = Facenet.InceptionResNetV2(dimension = 512)

    #-------------------------

    home = functions.get_deepface_home()

    if os.path.isfile('facenet512_weights.h5') != True:
        print("facenet512_weights.h5 will be downloaded...")

        output = 'facenet512_weights.h5'
        gdown.download(url, output, quiet=False)

    #-------------------------

    model.load_weights('facenet512_weights.h5')

    #-------------------------

    return model
