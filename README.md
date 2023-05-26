# Explicação do Código rgb.py <h2>
  
  
Este código em Python utiliza a biblioteca PIL (Python Imaging Library) para abrir uma imagem do arquivo **"ornitorrinco_original.jpg"** localizado na pasta "images". A imagem é armazenada na variável `img`.

A biblioteca PIL é comumente usada para manipular imagens em Python. Ela fornece uma série de funcionalidades para carregar, editar e salvar imagens em vários formatos.

A função `Image.open()` é usada para abrir a imagem especificada pelo caminho do arquivo. Neste caso, a imagem **"ornitorrinco_original.jpg"** é aberta. A função retorna um objeto Image que contém a imagem carregada.

Por fim, a imagem carregada é atribuída à variável `img`, que pode ser usada posteriormente para realizar várias operações de manipulação de imagem, como redimensionamento, rotação, aplicação de filtros, entre outros.
  
# Explicação do Código convert_grey.py <h2>
  
Neste código, estamos utilizando a biblioteca PIL (Python Imaging Library) para manipular imagens. Primeiro, importamos a classe `Image` do módulo `PIL`. Em seguida, utilizamos o método `open()` para carregar a imagem original localizada no diretório "images/ornitorrinco_original.jpg".

Depois disso, utilizamos o método `convert()` para converter a imagem para tons de cinza. A imagem resultante é armazenada na variável `img_grey`.

Por fim, utilizamos o método `save()` para salvar a imagem em tons de cinza no arquivo "images/ornitorrinco_grey.jpg".


# Explicação do Código grey_to_wb.py <h2> 
  
  
Neste código, estamos utilizando a biblioteca PIL (Python Imaging Library) para manipular imagens. Primeiro, importamos a classe `Image` do módulo `PIL`. Em seguida, utilizamos o método `open()` para carregar a imagem em tons de cinza localizada no diretório "images/ornitorrinco_grey.jpg".

Em seguida, definimos o limite de intensidade dos pixels usando a variável `limite`.

A linha seguinte utiliza o método `point()` para converter a imagem para preto e branco. Usamos uma função lambda para definir a lógica de conversão: se o valor do pixel for menor que o limite, ele é definido como 0 (preto), caso contrário, é definido como 255 (branco). O argumento `"1"` indica que queremos uma imagem binária (preto e branco).

Por fim, utilizamos o método `save()` para salvar a imagem em preto e branco no arquivo "images/ornitorrinco_wb.jpg".


  # Explicação do Código average_filter.py <h2> 
  
Neste código, estamos utilizando a biblioteca PIL (Python Imaging Library) para manipular imagens. Primeiro, importamos a classe `Image` do módulo `PIL`. Em seguida, utilizamos o método `open()` para carregar a imagem original localizada no diretório "images/ornitorrinco_original.jpg".

Criamos uma cópia da imagem original usando o método `copy()` para armazenar a imagem filtrada.

Definimos o tamanho do kernel do filtro de média com a variável `tamanho_kernel`. Neste exemplo, o kernel tem tamanho 3x3.

Em seguida, aplicamos o filtro de média percorrendo cada pixel da imagem original. Para cada pixel, extraímos uma matriz de pixels vizinhos com base no tamanho do kernel. Lidamos corretamente com os pixels nas bordas da imagem, preenchendo com preto (RGB: 0, 0, 0) se estiverem fora dos limites.

Calculamos a média dos valores RGB dos pixels vizinhos e atualizamos o pixel correspondente na imagem filtrada usando o método `putpixel()`.

Por fim, utilizamos o método `save()` para salvar a imagem filtrada no arquivo "images/ornitorrinco_average.jpg".


   # Explicação do Código median_filter.py <h2>
  
  
Neste código, estamos utilizando a biblioteca PIL (Python Imaging Library) para manipular imagens. Importamos as classes `Image` do módulo `PIL` e `median` do módulo `statistics`.

Em seguida, definimos a função `aplicar_filtro_mediana`, que recebe a imagem original, a imagem filtrada e o tamanho da janela do filtro como parâmetros. Essa função percorre cada pixel da imagem (exceto os pixels nas bordas) e aplica o filtro da mediana.

Dentro do loop, criamos uma lista `pixels_janela` para armazenar os pixels da janela em torno do pixel atual. Percorremos os índices da janela e adicionamos os pixels correspondentes na lista.

Ordenamos a lista `pixels_janela` e selecionamos o valor do pixel mediano (valor central) da lista.

Em seguida, utilizamos o método `putpixel()` para atualizar o pixel correspondente na imagem filtrada com o valor do pixel mediano.

No código principal, abrimos a imagem original com o método `open()` e criamos uma nova imagem filtrada do mesmo tamanho e modo.

Definimos o tamanho da janela do filtro com a variável `tamanho_janela`.

Chamamos a função `aplicar_filtro_mediana` passando a imagem original, a imagem filtrada e o tamanho da janela como parâmetros.

Por fim, utilizamos o método `save()` para salvar a imagem filtrada no arquivo "images/ornitorrinco_median.jpg".


  
  # Explicação do Código gaussian_filter.py <h2>
  
  
Neste código, estamos utilizando a biblioteca PIL (Python Imaging Library) para manipular imagens, bem como o módulo `numpy` para realizar operações eficientes em matrizes.

A função `gaussian_blur` recebe a imagem original e o raio do filtro gaussiano como parâmetros. Ela converte a imagem em uma matriz NumPy, cria o kernel gaussiano usando a função `_create_gaussian_kernel`, aplica o filtro gaussiano à matriz da imagem usando a função `_apply_gaussian_filter` e converte a matriz filtrada de volta para uma imagem PIL. A imagem filtrada é então retornada.

A função `_create_gaussian_kernel` cria um kernel gaussiano com base no raio fornecido. Ela itera sobre os índices do kernel, calcula o peso de cada posição usando a fórmula gaussiana e normaliza o kernel para que a soma dos valores seja igual a 1.

A função `_apply_gaussian_filter` aplica o filtro gaussiano a cada pixel da imagem. Ela itera sobre os pixels internos da imagem, extrai a vizinhança do pixel, aplica o filtro ponderado pela vizinhança e pelo kernel e atribui o valor filtrado ao pixel correspondente na matriz da imagem filtrada.

No código principal, abrimos a imagem original usando o método `open()` da classe `Image`. Em seguida, chamamos a função `gaussian_blur` passando a imagem original e o valor do raio (10) como parâmetros. A imagem filtrada é salva no arquivo "images/elephant_gaussian.jpg" usando o método `save()`.


  
  # Explicação do Código brightness.py <h2>
  
  
Neste código, estamos utilizando a biblioteca PIL (Python Imaging Library) para manipular imagens.

Primeiro, carregamos a imagem desejada usando o método `open()` da classe `Image` e passando o caminho para a imagem "images/ornitorrinco_original.jpg".

Definimos um fator de brilho (`fator = 3.5`) para ajustar o brilho da imagem. Você pode modificar esse valor de acordo com suas necessidades.

Em seguida, usamos o método `load()` para obter os pixels da imagem, permitindo manipulá-los diretamente.

Obtemos o tamanho da imagem usando o atributo `size` da imagem, que retorna uma tupla contendo a largura e a altura.

Em seguida, percorremos cada pixel da imagem usando dois loops aninhados, onde `i` percorre a largura e `j` percorre a altura.

Dentro do loop, obtemos a cor do pixel usando `pixels[i,j]`. A cor é representada como uma tupla (R, G, B) contendo os valores dos componentes de cor vermelho, verde e azul.

Ajustamos o valor de cada componente de cor multiplicando-o pelo fator de brilho e convertendo-o para um valor inteiro usando `int()`. Usamos uma list comprehension para realizar essa operação em cada componente de cor.

Em seguida, definimos a nova cor do pixel como uma tupla contendo os novos valores de cor ajustados.

No final do loop, atribuímos a nova cor ao pixel usando `pixels[i,j]`.

Por fim, salvamos a imagem resultante usando o método `save()`, passando o caminho para o arquivo de saída "images/ornitorrinco_brightness.jpg".


  
  # Explicação do Código contrast.py <h2>
  
  
Neste código, estamos utilizando a biblioteca PIL (Python Imaging Library) para manipular imagens.

Primeiro, carregamos a imagem desejada usando o método `open()` da classe `Image` e passando o caminho para a imagem "images/ornitorrinco_original.jpg".

Definimos um fator de brilho (`fator = 3.5`) para ajustar o contraste da imagem. Você pode modificar esse valor de acordo com suas necessidades.

Em seguida, usamos o método `load()` para obter os pixels da imagem, permitindo manipulá-los diretamente.

Obtemos o tamanho da imagem usando o atributo `size` da imagem, que retorna uma tupla contendo a largura e a altura.

Em seguida, percorremos cada pixel da imagem usando dois loops aninhados, onde `i` percorre a largura e `j` percorre a altura.

Dentro do loop, obtemos a cor do pixel usando `pixels[i,j]`. A cor é representada como uma tupla (R, G, B) contendo os valores dos componentes de cor vermelho, verde e azul.

Ajustamos o valor de cada componente de cor usando a fórmula de ajuste de contraste `(c - 128) * fator + 128`, onde `c` é o valor do componente de cor. Essa fórmula subtrai 128 do valor do componente de cor para centrar a escala em torno do valor médio de 128, aplica o fator de brilho e adiciona 128 novamente para reverter o deslocamento.

Usamos uma list comprehension para realizar essa operação em cada componente de cor.

Em seguida, definimos a nova cor do pixel como uma tupla contendo os novos valores de cor ajustados.

No final do loop, atribuímos a nova cor ao pixel usando `pixels[i,j]`.

Por fim, salvamos a imagem resultante usando o método `save()`, passando o caminho para o arquivo de saída "images/ornitorrinco_contrast.jpg".

  
  # Explicação do Código rotate.py <h2>
  
  
Neste código, estamos utilizando a biblioteca PIL (Python Imaging Library) para manipular imagens.

Primeiro, abrimos a imagem desejada usando o método `open()` da classe `Image` e passando o caminho para a imagem "images/ornitorrinco_original.jpg".

Em seguida, utilizamos o método `rotate()` para girar a imagem em 90 graus no sentido horário. O parâmetro `expand=True` permite que a imagem seja redimensionada para acomodar o conteúdo girado, evitando a perda de informações.

Criamos uma nova imagem chamada `nova_imagem` com o tamanho necessário para conter a imagem girada. Para isso, utilizamos o método `new()` da classe `Image` e passamos os argumentos 'RGBA' (indicando que a imagem terá componentes de cor vermelho, verde, azul e alfa) e o tamanho da imagem girada (`imagem_rotate.size`). Definimos a cor de fundo como transparente, passando a tupla `(255, 255, 255, 0)`.

Determinamos a posição para colar a imagem girada no centro da nova imagem. Para isso, calculamos as coordenadas `posicao` utilizando a diferença entre os tamanhos da nova imagem e da imagem girada, dividindo por 2 para obter o deslocamento necessário.

Em seguida, utilizamos o método `paste()` da imagem `nova_imagem` para colar a imagem girada (`imagem_rotate`) na posição definida (`posicao`).

Por fim, salvamos a imagem girada utilizando o método `save()` da imagem `imagem_rotate`, passando o caminho para o arquivo de saída "images/ornitorrinco_rotate.jpg".

  
  # Explicação do Código flip.py <h2>
  
  
Neste código, estamos utilizando a biblioteca PIL (Python Imaging Library) para manipular imagens.

Primeiro, abrimos a imagem desejada usando o método `open()` da classe `Image` e passando o caminho para a imagem "images/ornitorrinco_original.jpg".

Em seguida, utilizamos o método `transpose()` da imagem para inverter a imagem na horizontal. Passamos o argumento `Image.FLIP_LEFT_RIGHT` para indicar que queremos realizar a inversão na horizontal (flip left-right).

Criamos uma nova imagem chamada `imagem_invertida` que contém a imagem original invertida na horizontal.

Por fim, utilizamos o método `save()` da imagem `imagem_invertida` para salvar a imagem resultante. Passamos o caminho para o arquivo de saída "images/ornitorrinco_flip_leftright.jpg".


