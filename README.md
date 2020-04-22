# Text Analysis :squirrel:

### _Programa em python que realiza análise em texto usando recursos da API [Algorithmia](https://algorithmia.com)_

[![CodeFactor](https://www.codefactor.io/repository/github/mateusfg7/textanalysis/badge)](https://www.codefactor.io/repository/github/mateusfg7/textanalysis)

_Index_

1. [Funções](#funções)
2. [Dependências](#dependências)
    - [Arquivo de Dependências](#instale-usando-o-arquivo-de-dependências-do-python)
    - [Dependências Separadas](#instale-as-dependências-separadamente)
3. [Uso](#uso)
    - [Exêmplos de Uso](#exêmplos-de-uso)

---

## Funções:

-   Obter tags a partir de um texto.

-   Obter grau de sentimentos positivos, negativos e neutros.

-   Resumir um texto.

-   Obter nomes de entidades presentes no texto.

-   Obter a frequência de determinadas palavras em um texto.

## Dependências:

### _Instale usando o arquivo de dependências do Python:_

```
python3 -m pip install -r requirements.txt
```

### **Ou**

### _instale as dependências separadamente:_

**Algorithmia**

```
pip3 install algorithmia
```

**GoogleTrans**

```
pip3 install googletran
```

## Uso

`analysis.py --file [arquivo] [opção]`

`--tag` pegar tags

`--feeling` obter sentimentos negativos, positivos e neutros

`--summarize` resumir um texto

`--count` contar palavras

`--entity` reconhecer nomes de entidades

`--frequency` calcular a frequência das n palavras mais comuns de um texto
(`analysis.py --file [arquivo] --frequency [nº de palavras analisadas]`)

#### Exêmplos de uso:

1 - extrair tags em um texto no arquivo 'turing.txt'

_in:_

```shell
$ python3 analysis.py --file turing.txt --tag
```

_out:_

```shell
['após', 'computação', 'foi', 'para', 'pela', 'química', 'turing', 'uma']
```

2 - pegar a frequência das palavras mais comuns em um texto no arquivo 'turing.txt'

_in:_

```shell
$ python3 analysis.py --file turing.txt --frequency 5
```

_out:_

```shell
1ª Palavra: de
Frequência: 21

2ª Palavra: a
Frequência: 10

3ª Palavra: da
Frequência: 10

4ª Palavra: um
Frequência: 10

5ª Palavra: e
Frequência: 8
```
