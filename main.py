import urllib.request as request
import numpy as np
import cv2
from PIL import Image
import time

url = 'http://192.168.0.110:8080/shot.jpg?rnd=274471'

while True:
    img = request.urlopen(url)
    img_type = bytearray(img.read())
    img_np = np.array(img_type, dtype=np.uint8)
    frame = cv2.imdecode(img_np, -1)
    frame_convert_color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_blur = cv2.GaussianBlur(frame_convert_color, (5, 5), 0)
    frame_edge = cv2.Canny(frame_blur, 30, 50)
    contours, _ = cv2.findContours(frame_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        
    cv2.imshow('My Smart scanner', frame_edge)
    if cv2.waitKey(1) == ord('s'):
        img_pil = Image.fromarray(frame)
        time_str = time.strftime('%Y-%m-%d-%H-%M-%S')
        img_pil.save(f'{time_str}.pdf')
        print(time_str)


    
   