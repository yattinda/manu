import qrcode

#a = input("Plz URL:")

img = qrcode.make(input("Plz URL:"))

img.save("qrcode/URL.png")
