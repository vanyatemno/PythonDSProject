from app.io.input import *
from app.io.output import *

def main():

    print("text read form the console:", getTextFromConsole())
    print()
    print("text read from file 'input.txt':")
    print(getTextFromFilePy('input.txt'), "\n")
    print("table read from file 'sample_csv.csv':",getTextFromFilePandas('sample_csv.csv'), "\n")
    print()

    print("output of function which writes data to console:")
    print(writeToConsole('mjav'))
    print()
    print("output fo function which writes data to file 'output.txt':", writeToFile('output.txt', 'mjav'))

if __name__ == "__main__":
    main()