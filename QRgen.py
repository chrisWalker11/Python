import pyqrcode
import png
s =  input("enter url for QR code: ")

url = pyqrcode.create(s)

url.png('myqr.png', scale = 6)
