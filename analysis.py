import sys

try:
    import Algorithmia
    CLIENT = Algorithmia.client('simC43S79CE5FQyQ35I6X8UWv3z1')
except ModuleNotFoundError:
    print("Biblioteca 'Algorithmia' não foi encontrada.")
    print("tente: pip3 install algorithmia")
    sys.exit(1)

from utils.readFile import read_file

from connection import checkInternetConnection as netCheck
from connection import internetFailWarning as netWarning

from functions.pegar_tags import pegar_tags
from functions.analise_de_sentimento import analise_de_sentimento
from functions.resumir_texto import resumir_texto
from functions.contar_palavras import contar_palavras
from functions.reconhecimento_de_entidades import reconhecimento_de_entidades
from functions.frequencia_de_palavras import frequencia_de_palavras


def menu():
    print(
        """
    Use: analysis.py [opção] [arquivo]

    -t  pegar tags apartir de um texto

    -s  obter sentimentos negativos, positivos e neutros apartir de um texto

    -r  resumir um texto

    -c  contar palavras contidas em um texto

    -e  reconhecer nomes de entidades

    -f calcular a frequência das n palavras mais comuns de um texto
        analysis.py -f [arquivo] [numero de palavras analisadas]
    """
    )


try:
    FIRST_ARGUMENT = sys.argv[1]
    SECOND_ARGUMENT = sys.argv[2]
except IndexError:
    menu()
    sys.exit()


def condicionais():
    try:
        if FIRST_ARGUMENT == "-t":
            if netCheck():
                pegar_tags(CLIENT, read_file(SECOND_ARGUMENT))
            else:
                netWarning()

        elif FIRST_ARGUMENT == "-s":
            if netCheck():
                analise_de_sentimento(CLIENT, read_file(SECOND_ARGUMENT))
            else:
                netWarning()

        elif FIRST_ARGUMENT == "-r":
            if netCheck():
                resumir_texto(CLIENT, read_file(SECOND_ARGUMENT))
            else:
                netWarning()

        elif FIRST_ARGUMENT == "-c":
            if netCheck():
                contar_palavras(CLIENT, read_file(SECOND_ARGUMENT))
            else:
                netWarning()

        elif FIRST_ARGUMENT == "-e":
            if netCheck():
                reconhecimento_de_entidades(
                    CLIENT, read_file(SECOND_ARGUMENT))
            else:
                netWarning()

        elif FIRST_ARGUMENT == "-f":
            if netCheck():
                frequencia_de_palavras(CLIENT, read_file(SECOND_ARGUMENT))
            else:
                netWarning()

        elif FIRST_ARGUMENT == "-h":
            menu()

    except IndexError:
        menu()


# main execution
condicionais()
