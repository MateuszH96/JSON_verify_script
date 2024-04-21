from .CustomExceptions import *

class VerifyJsonData:
    def __init__(self,data:dict) -> None:
        if not isinstance(data, dict):
            raise IncorrectDataType(f"Incorrect type data, given {type(data)}, dict is required")
        
        self.__data = data
    
    def verifyData(self) -> bool:
        if "PolicyName" not in self.__data.keys() or "PolicyDocument" not in self.__data.keys():
            raise IncompleteData(f"Incomplete data, PolicyDocument and PolicyName is required")
        
        if not isinstance(self.__data["PolicyDocument"], dict):
            raise IncorrectDataType(f"Incorrect type data, given {type(self.__data['PolicyDocument'])}, dict is required")
        
        if "Statement" not in self.__data["PolicyDocument"].keys():
            raise IncompleteData(f"Incomplete data, [\"PolicyDocument\"][\"Statement\"] is required")
        
        if not isinstance(self.__data["PolicyDocument"]["Statement"], list):
            raise IncorrectDataType(f"Incorrect type data, given {type(self.__data['PolicyDocument']['Statement'])}, list is required")
        
        for statment in self.__data['PolicyDocument']['Statement']:

            if "Resource" not in statment.keys():
                raise IncompleteData(f"Incomplete data, [\"PolicyDocument\"][\"Statement\"][i][\"Resource\"] is required")
            
            if isinstance(statment["Resource"], str) and statment["Resource"] == "*":
                return False
            
        return True