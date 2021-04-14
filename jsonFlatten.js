import sys
import json


# some JSON:
jsonString =  '{"a": 1,"b": true, "c": {"d": 3, "e": "test"}}'

# parse jsonString:
myJson = json.loads(jsonString)



for key in myJson:
    print(type(myJson[key]))
    if type(myJson[key]) == dict:
        print(key, ":", myJson[key])









# Readme: python 3.8, Time()