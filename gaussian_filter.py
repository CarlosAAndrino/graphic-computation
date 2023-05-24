from PIL import Image
import numpy as np
import math


def gaussian_blur(image, radius):
    # Converte a imagem em uma matriz NumPy
    img_array = np.array(image)

    # Calcula o tamanho do kernel com base no raio
    size = int(radius) * 2 + 1

    # Cria o kernel Gaussiano
    kernel = _create_gaussian_kernel(radius)

    # Aplica o filtro Gaussiano à matriz da imagem
    blurred_array = _apply_gaussian_filter(img_array, kernel)

    # Converte a matriz de volta para uma imagem PIL
    blurred_image = Image.fromarray(blurred_array)

    return blurred_image


def _create_gaussian_kernel(radius):
    size = int(radius) * 2 + 1
    kernel = np.zeros((size, size))
    sigma = radius / 3

    for x in range(size):
        for y in range(size):
            distance = math.sqrt((x - radius)**2 + (y - radius)**2)
            weight = math.exp(-(distance ** 2) / (2 * sigma ** 2))
            kernel[x, y] = weight

    # Normaliza o kernel para que a soma dos valores seja igual a 1
    kernel /= np.sum(kernel)

    return kernel


def _apply_gaussian_filter(image_array, kernel):
    # Extrai as dimensões da imagem e do kernel
    image_height, image_width, _ = image_array.shape
    kernel_size = kernel.shape[0]
    border = kernel_size // 2

    # Cria uma cópia da matriz da imagem para armazenar o resultado filtrado
    filtered_array = image_array.copy()

    # Aplica o filtro Gaussiano a cada pixel da imagem
    for i in range(border, image_height - border):
        for j in range(border, image_width - border):
            # Obtém a vizinhança do pixel
            neighborhood = image_array[i - border:i +
                                       border + 1, j - border:j + border + 1, :]

            # Aplica o filtro ponderado pela vizinhança e pelo kernel
            filtered_pixel = np.sum(
                neighborhood * kernel[:, :, np.newaxis], axis=(0, 1))

            # Atribui o valor filtrado ao pixel na imagem filtrada
            filtered_array[i, j, :] = filtered_pixel

    return filtered_array.astype(np.uint8)


imagem = Image.open("images/elephant.jpg")
imagem_desfocada = gaussian_blur(imagem, 10)
imagem_desfocada.save("images/elephant_gaussian.jpg")