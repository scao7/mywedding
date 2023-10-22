import qrcode
img = qrcode.make('https://shengtingcao.top/mywedding/')
type(img)  # qrcode.image.pil.PilImage
img.save("qrcode.png")