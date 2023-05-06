from PIL import Image

# importando imagem
img = Image.open("images/ornitorrinco_original.jpg")

# convertento para tons de cinza
img_grey = img.convert("L")

# salvando imagem
img_grey.save("images/ornitorrinco_grey.jpg")