import qrcode

img = qrcode.make("https://github.com/PiyushAggarwal01")
img.save("piyush_github.png")

print("QR Code Created Successfully!")