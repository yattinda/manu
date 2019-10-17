import qrcode

img = qrcode.make("https://yattinda.github.io/")

img.save("myhome.png")
