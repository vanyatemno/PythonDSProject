import pandas

def getTextFromConsole():
    """
    Function, which gets input from a console
    :return: (str) - read input text from console
    """
    userInput = input("Please, enter your input: ")
    return userInput

def getTextFromFilePy(filename):
    """
    Function, which gets text from the specified file
    :param fileanme: (str) name of a file to read text from
    :return: (str) text of specified file
    """

    res = ""

    with open(f"./data/{filename}") as file:
        for line in file:
            res += line

    return res

def getTextFromFilePandas(filename):
    """
    Function, which gets text from the specified file
    :param filename: (str) name of a file to read text from
    :return: (str) text of specified file
    """
    csvFile = pandas.read_csv(f"./data/{filename}")

    return csvFile



