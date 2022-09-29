import urllib.request as request
from PIL import Image
url = 'http://192.168.0.112:8080/shot.jpg?rnd=99891'

while True:
    img = request.urlopen(url)
    img2 = Image.open(img)
    img2.show()
    
    s = str(input())
    if s =='s':
        break
    
