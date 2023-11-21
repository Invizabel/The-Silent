import io
import urllib.parse
import face_recognition
import numpy as np
from PIL import Image

def read(data,host):
    host = urllib.parse.urlparse(host).netloc + urllib.parse.urlparse(host).path.replace("/","{}")
    image = np.array(Image.open(io.BytesIO(data)))
    face_locations = face_recognition.face_locations(image)
    face_count = 0
    for _ in face_locations:
        face_count += 1
        top,right,bottom,left = _
        img = image[top:bottom,left:right]
        pil_image = Image.fromarray(img)
        pil_image.save(f"image {face_count}: {host}.png")
