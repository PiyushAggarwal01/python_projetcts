import qrcode
from PIL import Image
# img = qrcode.make("https://github.com/PiyushAggarwal01")
# img.save("piyush_github.png")

# print("QR Code Created Successfully!")
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border = 4,)
qr.add_data("https://www.linkedin.com/in/piyush-aggarwal-b51544324/")
qr.make(fit=True)
img = qr.make_image(fill_color = "red", back_color = "blue")
img.save("piyush_linkin.png")
