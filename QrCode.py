#!/usr/bin/python3

#sudo apt install python3-qrcode

#1
import qrcode

Url="https://colibrispropretesaintjoseph.blogspot.com"
img = qrcode.make(Url)

print (type(img))
print (img.size)
img.save("/home/antoine/Bureau/qrcode.png")

#2 more options and details
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=3,
    border=2
)

qr.add_data(Url)
qr.make()
img = qr.make_image(fill_color="black", back_color="#FFFFFF")
img.save("/home/antoine/Bureau/qrcode2.png")
