from PIL import Image

# Carrega a imagem desejada
imagem = Image.open("images/ornitorrinco_original.jpg")

# Inverte a imagem na vertical
imagem_invertida = imagem.transpose(Image.FLIP_TOP_BOTTOM)

# Salva a imagem resultante
imagem_invertida.save("images/ornitorrinco_flip_topbottom.jpg")
