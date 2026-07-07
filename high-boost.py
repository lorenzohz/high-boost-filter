import sys
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, img_as_float, img_as_ubyte
from scipy.ndimage import uniform_filter

def filtro_high_boost(imagem, m, k):
    """
    Aplica o filtro High-Boost em uma imagem em tons de cinza.
    """
    img_float = img_as_float(imagem)
    img_borrada = uniform_filter(img_float, size=m)
    mascara = img_float - img_borrada
    img_aguçada = img_float + (k * mascara)
    img_final = np.clip(img_aguçada, 0, 1)
    
    return img_final, mascara


if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("Formato esperado: python high-boost.py <caminho_imagem> <m> <k>")
        print("Exemplo: python high-boost.py imagem.png 5 2.5")
        sys.exit(1)

    # Parâmetros
    caminho_imagem = sys.argv[1]
    
    try:
        m = int(sys.argv[2])
        k = float(sys.argv[3])
    except ValueError:
        print("Erro de tipo de dado")
        print("O parâmetro 'm' deve ser um número inteiro (ex: 3, 5).")
        print("O parâmetro 'k' deve ser um número decimal (ex: 1.5, 2.0).")
        sys.exit(1)

    print(f"Processando '{caminho_imagem}' com m={m} e k={k}...")

    # Carregar imagem
    try:
        imagem_original = io.imread(caminho_imagem, as_gray=True)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_imagem}' não foi encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro inesperado ao abrir a imagem: {e}")
        sys.exit(1)

    # Aplicar filtro
    resultado, mascara_detalhes = filtro_high_boost(imagem_original, m=m, k=k)

    # Normalizar máscara para salvá-la
    mascara_normalizada = (mascara_detalhes - mascara_detalhes.min()) / (mascara_detalhes.max() - mascara_detalhes.min())

    # Salvar
    saida_mascara = f"mascara_m{m}_k{k}.png"
    saida_imagem = f"resultado_m{m}_k{k}.png"
    io.imsave(saida_imagem, img_as_ubyte(resultado))
    io.imsave(saida_mascara, img_as_ubyte(mascara_normalizada))
    print(f"Sucesso! Imagem salva como '{saida_imagem}'. Máscara normalizada salva como '{saida_mascara}'.")