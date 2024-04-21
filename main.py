import argparse
from source_module.CustomExceptions import *
from source_module.ReadJsonFile import ReadJsonFile
from source_module.VerifyJsonData import VerifyJsonData

def verifyInputData(filePath:str) -> bool:
    readFile = ReadJsonFile(filePath)
    verifyData = VerifyJsonData(readFile.getData())
    return verifyData.verifyData()

def main() -> None:
    parser = argparse.ArgumentParser(description="read file at this path")
    parser.add_argument('pathToFile',metavar='pathToFile',type=str, help='enter path to your file')
    args = parser.parse_args()
    filePath = args.pathToFile

    if verifyInputData(filePath):
        print("Correct value")
    else:
        print("Incorrect value")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)