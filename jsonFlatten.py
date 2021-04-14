import sys
import json


# Test JSON string
json_string =  '{"a": 1,"b": true, "c": {"d": 3, "e": "test"}, "f": {"g": 5, "h": "hello", "i": {"j": false, "k": "okay"}}}'

# Convert JSON string to object
my_json = json.loads(json_string)

output_json_string = '{}'

output_json =json.loads(output_json_string)




# 
def read_nested_json(previous_key , nested_json):
    for key in nested_json:
        if type(nested_json[key]) == dict:
            new_key = previous_key+"."+key
            read_nested_json(new_key, nested_json[key])   
        else:
            new_key = previous_key+"."+key
            output_json[new_key] = nested_json[key]
            print(previous_key+"."+key, ":", nested_json[key])
    return True



#
for key in my_json:
    if type(my_json[key]) == dict:
        read_nested_json(key, my_json[key])   
    else:
        output_json[key] = my_json[key]
        print(key, ":", my_json[key])


for key in output_json:
        print(key, ":", output_json[key])

print(json.dumps(output_json))




# Readme: python 3.8, Time()