import urllib.request as request
import numpy as np
import cv2

url = 'http://192.168.0.112:8080/shot.jpg?rnd=163311'

while True:
    img = request.urlopen(url)
    img_type = bytearray(img.read())
    img_np = np.array(img_type, dtype=np.uint8)
    frame = cv2.imdecode(img_np, -1)
    cv2.imshow('My Smart scanner', frame)
    cv2.waitKey(1)
    

    
   