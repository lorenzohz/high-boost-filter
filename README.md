# Filtro High-Boost em Python

Um script simples em Python para aplicar o Filtro High-Boost (e Unsharp Masking) em imagens. Este projeto utiliza processamento espacial para realçar bordas, texturas e detalhes finos em fotografias e documentos.

O script foi desenvolvido baseando-se nas equações clássicas de processamento digital de imagens (como descrito por Gonzalez & Woods), garantindo o tratamento correto de valores negativos na máscara de nitidez e a conversão segura de tipos de dados.

## Funcionalidades
* Aplica o filtro espacial High-Boost via linha de comando (CLI).
* Aceita parâmetros customizáveis para o tamanho da máscara matemática (m) e o peso do realce (k).
* Conversão automática: Aceita imagens coloridas ou nativas em tons de cinza e as processa automaticamente.
* Suporta múltiplos formatos (recomendado: .png).

## Pré-requisitos
Para rodar este script, você precisará do Python instalado e das seguintes bibliotecas científicas:

```
pip install numpy scipy scikit-image matplotlib
```

## Como usar

Execute o script diretamente pelo terminal, chamando o interpretador do Python, seguido do nome do arquivo e dos 3 parâmetros obrigatórios:

```
python high-boost.py <caminho_da_imagem> <m> <k>
```

Exemplo prático:

```
python high-boost.py imagens/minha_foto.png 5 2.0
```

Após a execução, o script processará a imagem e salvará o resultado automaticamente na mesma pasta, com o nome indicando os parâmetros utilizados (ex: resultado_m5_k2.0.png).

## Entendendo os Parâmetros

* caminho_da_imagem: O local onde sua imagem original está salva. Formatos sem perdas (lossless) como PNG são recomendados para evitar a amplificação de artefatos de compressão (comuns em JPGs de baixa qualidade).
* m (Tamanho da Máscara): Um número inteiro e ímpar (ex: 3, 5, 7, 9). Define a área de vizinhança que o filtro da média usará para borrar a imagem e extrair os detalhes. Valores muito altos podem criar halos ao redor de objetos.
* k (Peso / Fator de Boost): Um número decimal que define a agressividade do filtro.
  * k = 1.0: Executa o Unsharp Masking clássico (realce natural).
  * k > 1.0: Executa o High-Boost (realce agressivo).
