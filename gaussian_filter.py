from PIL import Image, ImageFilter

# abrir a imagem
imagem = Image.open("images/ornitorrinco_original.jpg")

# aplicar o filtro de desfoque gaussiano
imagem_desfocada = imagem.filter(ImageFilter.GaussianBlur(radius=2))

# salvar a imagem desfocada
imagem_desfocada.save("images/ornitorrinco_gaussian.jpg")
