import qrcode
qr = qrcode.QRCode()
data = "My name is jale saini....."
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("4.png")