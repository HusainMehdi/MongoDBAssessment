import sys
import json

output_json_string = '{}'
output_json = json.loads(output_json_string)

# Flattens and adds nested JSON values of input JSON to output JSON
def flatten_nested(previous_key , nested_json):
    for key in nested_json:
        if type(nested_json[key]) == dict:
            new_key = previous_key+"."+key
            flatten_nested(new_key, nested_json[key])   
        else:
            new_key = previous_key+"."+key
            output_json[new_key] = nested_json[key]

# Adds non-JSON values of input JSON to output JSON
def flatten(my_json):
    global output_json 
    output_json = {}
    for key in my_json:
        if type(my_json[key]) == dict:
            flatten_nested(key, my_json[key])   
        else:
            output_json[key] = my_json[key]
    return json.dumps(output_json)

# Reads the input JSON
def main():
    for line in sys.stdin:
        input_json_string = line
    input_json = json.loads(input_json_string)
    
    sys.stdout.write(flatten(input_json))

if __name__ == "__main__":
    main()

