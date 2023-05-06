from PIL import Image

# abrir a imagem
imagem = Image.open("images/ornitorrinco_original.jpg")

# criar uma cópia da imagem
imagem_filtrada = imagem.copy()

# definir o tamanho do kernel do filtro de média
tamanho_kernel = 3

# aplicar o filtro de média
for x in range(imagem.width):
    for y in range(imagem.height):
        # extrair uma matriz de pixels do tamanho do kernel ao redor do pixel atual
        pixels = []
        for i in range(-tamanho_kernel // 2, tamanho_kernel // 2 + 1):
            for j in range(-tamanho_kernel // 2, tamanho_kernel // 2 + 1):
                # lidar com pixels nas bordas da imagem
                if x + i < 0 or x + i >= imagem.width or y + j < 0 or y + j >= imagem.height:
                    pixels.append((0, 0, 0))
                else:
                    pixels.append(imagem.getpixel((x + i, y + j)))
        # calcular a média dos valores dos pixels vizinhos
        r = sum([p[0] for p in pixels]) // len(pixels)
        g = sum([p[1] for p in pixels]) // len(pixels)
        b = sum([p[2] for p in pixels]) // len(pixels)
        # atualizar o pixel na imagem filtrada
        imagem_filtrada.putpixel((x, y), (r, g, b))

# salvar a imagem filtrada
imagem_filtrada.save("images/ornitorrinco_average.jpg")
