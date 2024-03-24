def writeToConsole(text):
    """
    Function to write text to a console
    :param text: (str) text to write to a console
    :return: nothing
    """

    print(text)

def writeToFile(filename, text):
    """
    Function which writes some text to specified file
    :param filename: (str) name of a file to write text to
    :param text: (str) message to write to file
    :return: nothing
    """

    with open(f'./data/{filename}', 'w') as file:
        file.write(text)