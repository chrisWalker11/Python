import pyqrcode
import png
s =  input("enter url for QR code: ")

url = pyqrcode.create(s)

url.png(input("enter name for QR code: ") + '.png', scale = 6)
