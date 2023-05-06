from PIL import Image

# Carrega a imagem desejada
imagem = Image.open("images/ornitorrinco_original.jpg")

# Fator de brilho
fator = 3.5

# Obtém os pixels da imagem
pixels = imagem.load()

# Obtém tamanho da imagem
largura, altura = imagem.size

# Percorre cada pixel da imagem e ajusta o brilho
for i in range(largura): # Largura da imagem
    for j in range(altura): # Altura da imagem
        # Obtém a cor do pixel (R, G, B)
        cor = pixels[i,j]

        # Ajusta o valor de cada componente de cor r,g,b com o brilho
        nova_cor = tuple([int(c * fator) for c in cor])

        # Define a nova cor do pixel
        pixels[i,j] = nova_cor

# Salva a imagem resultante
imagem.save("images/ornitorrinco_brightness.jpg")
