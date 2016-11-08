import numpy as np
import urllib
import cv2

def get_image(url):
    resp = urllib.urlopen(url)
    data = resp.read()
    image = np.asarray(bytearray(data), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image