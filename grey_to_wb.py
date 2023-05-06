from PIL import Image

# importando imagem em tons de cinza
img = Image.open("images/ornitorrinco_grey.jpg")

# intensidade dos pixels
limite = 80

# converter para preto e branco com o calculo do limite do pixel para identificar o que será branco ou preto
img_whiteblack = img.point(lambda x: 0 if x < limite else 255, "1")

# salvar a imagem preta e branca
img_whiteblack.save("images/ornitorrinco_wb.jpg")