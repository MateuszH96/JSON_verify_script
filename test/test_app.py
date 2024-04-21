import os 
import pytest
from source_module.ReadJsonFile import ReadJsonFile
from source_module.VerifyJsonData import VerifyJsonData
from source_module.CustomExceptions import *


def test_incorrect_path_file():
    with pytest.raises(FileDoesNotExists) as exc:
        readJSONfile = ReadJsonFile('dummy_data')

def test_is_read_correct_data():
    readJSONfile = ReadJsonFile(os.path.join(os.getcwd(),'ReadFiles','simpleData.json'))
    assert readJSONfile.getData() == {"data": "sample"}

def test_is_type_is_not_correct():
    with pytest.raises(IncorrectDataType) as exc:
        verifyJSONdata = VerifyJsonData('dummy_data')
        
def test_is_policy_data_is_incomplete():
    with pytest.raises(IncompleteData) as exc:
        verifyJSONdata = VerifyJsonData({'dummy':'data'})
        verifyJSONdata.verifyData()
        
def test_is_PolicyName_data_is_not_correct():
    with pytest.raises(IncorrectDataType) as exc:
        verifyJSONdata = VerifyJsonData({"PolicyName" : "dummy",
                                "PolicyDocument" : "data"})
        verifyJSONdata.verifyData()

def test_is_PolicyName_data_is_incomplete():
    with pytest.raises(IncompleteData) as exc:
        verifyJSONdata = VerifyJsonData({"PolicyName" : "dummy",
                                "PolicyDocument" : {"data":"dummy"}})
        verifyJSONdata.verifyData()

def test_is_Statement_data_is_not_correct():
    with pytest.raises(IncorrectDataType) as exc:
        verifyJSONdata = VerifyJsonData({"PolicyName" : "dummy",
                                "PolicyDocument" : {"Statement":"data"}})
        verifyJSONdata.verifyData()

def test_is_Statement_data_is_incomplete():
    with pytest.raises(IncompleteData) as exc:
        verifyJSONdata = VerifyJsonData({"PolicyName" : "dummy",
                                "PolicyDocument" : {"Statement":[{"dummy":"data"}]}})
        verifyJSONdata.verifyData()

def test_is_Resource_is_asterisk():
    readJSONfile = ReadJsonFile(os.path.join(os.getcwd(),'ReadFiles','input.json'))
    verifyJSONdata = VerifyJsonData(readJSONfile.getData())
    assert verifyJSONdata.verifyData() == False

def test_is_Resource_is_non_asterisk_string():
    readJSONfile = ReadJsonFile(os.path.join(os.getcwd(),'ReadFiles','input1.json'))
    verifyJSONdata = VerifyJsonData(readJSONfile.getData())
    assert verifyJSONdata.verifyData() == True

def test_is_Resource_is_non_asterisk_string():
    readJSONfile = ReadJsonFile(os.path.join(os.getcwd(),'ReadFiles','input2.json'))
    verifyJSONdata = VerifyJsonData(readJSONfile.getData())
    assert verifyJSONdata.verifyData() == True
