import sys

from interface import texts

from utils.fileTreatment import readFile
from utils.connection import checkInternetConnection as netCheck
from utils.connection import internetFailWarning as netWarning

from functions.getTags import getTags
from functions.feelingAnalisys import feelingAnalisys
from functions.summarizeText import summarizeText
from functions.countWords import countWords
from functions.entityRecognition import entityRecognition
from functions.frequencyOfWords import frequencyOfWords
from functions.emailExtract import emailExtract


def choices(option, client, file):
    fileState = readFile(file)

    if fileState:
        try:
            if netCheck():

                "c: client ; f: file"
                optionSelect = {
                    "--tag": lambda c, f: getTags(c, f),
                    "--feeling": lambda c, f: feelingAnalisys(c, f),
                    "--summarize": lambda c, f: summarizeText(c, f),
                    "--count": lambda c, f: countWords(c, f),
                    "--entity": lambda c, f: entityRecognition(c, f),
                    "--frequency": lambda c, f: frequencyOfWords(c, f),
                    "--email": lambda c, f:  emailExtract(c, f)
                }
                optionSelect[option](client, fileState)

            else:
                netWarning()

        except IndexError:
            print(texts.menu())
    else:
        print(f'Arquivo "{file}" não encontrado!\n')
        print(texts.menu())
        sys.exit(1)
