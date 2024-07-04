import qrcode
import image
qr = qrcode.QRCode(
    version= 10,
    box_size = 5,
    border=4
)
data = "https://www.google.com/maps/@8.9892901,38.7576607,11.72z?entry=ttu"
qr.add_data(data)
qr.make(fit=True)
img= qr.make_image(fill="black",back_color="white")
img.save("test.png")