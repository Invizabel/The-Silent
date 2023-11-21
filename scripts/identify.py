import io
import os
import numpy as np
import face_recognition
from PIL import Image

def read(data):
    try:
        files = os.listdir()
        for _ in files:
            if _.startswith("compare"):
                file = _
                break
        compare_image = face_recognition.load_image_file(file)
        unknown_image = np.array(Image.open(io.BytesIO(data)))
        compare_image = face_recognition.face_encodings(compare_image)[0]
        unknown_image = face_recognition.face_encodings(unknown_image)[0]
        result = face_recognition.compare_faces([compare_image], unknown_image)
        return str(result[0])

    except:
        return "False"
