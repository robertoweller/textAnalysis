def menu():
    return (
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


def moduleNotFoundError(moduleName, modulePackage):
    return(
        f"""
    Biblioteca '{moduleName}' não foi encontrada.
    tente: pip3 install {modulePackage}
        """
    )


def optionsTitle(option):
    textOfOptions = {
        '--tag': '\nPegando tags...\n',
        '--feeling': '\nFazendo análise de sentimentos...\n',
        '--summarize': '\nResumindo texto...\n',
        '--count': '\nContando palavras...\n',
        '--entity': '\nExtraindo entidades...\n',
        '--frequency': '\nObtendo frequencia de cada palavra...\n',
    }
    return textOfOptions[option]
