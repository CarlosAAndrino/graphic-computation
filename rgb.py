from PIL import Image

# importando imagem
img = Image.open("images/ornitorrinco_original.jpg")

# separando os canais r,g,b
r, g, b = img.split()

# salvando cada canal
r.save("images/ornitorrinco_r.jpg")
g.save("images/ornitorrinco_g.jpg")
b.save("images/ornitorrinco_b.jpg")
