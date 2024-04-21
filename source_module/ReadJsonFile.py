from .CustomExceptions import *
import os
import json
class ReadJsonFile:
    def __init__(self, pathFile) -> None:
        if not os.path.isfile(pathFile):
            raise FileDoesNotExists(f"File at '{pathFile}' does not exists")
        
        file = open(pathFile, "r")
        self.__data = json.load(file)
        file.close()
    
    def getData(self):
        return self.__data