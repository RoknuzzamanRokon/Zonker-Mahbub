import urllib.request as request
import numpy as np
import cv2
from PIL import Image

url = 'http://192.168.0.110:8080/shot.jpg?rnd=274471'

while True:
    img = request.urlopen(url)
    img_type = bytearray(img.read())
    img_np = np.array(img_type, dtype=np.uint8)
    frame = cv2.imdecode(img_np, -1)
    cv2.imshow('My Smart scanner', frame)
    if cv2.waitKey(1) == ord('s'):
        img_pil = Image.fromarray(frame)
        img_pil.save('My_Scanned_file.pdf')
        print("Save")
    

    
   