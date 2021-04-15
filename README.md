# MongoDBAssessment

json_flatten.py will convert a JSON with nested JSONs inside it into a flat JSON

 
## Time Taken: 5 hours, 30 minutes

### Further Context
It took me about 5 hours 30 minutes, including researching (e.g. Python JSON library).
I did this in two sittings: 
- The first sitting was at the end of a day of fasting and I was more tired and slow-moving than usual and so decided to pause overnight.
- This afternoon I spent another 2.5 hours on it.


## Written with Python 3.8

## Running the code
The code can be run using:

cat your_input.json | python json_flatten.py

where your_input.json is the input JSON file.


## Writing output to a file
The JSON output can be written to a file using:

cat your_input.json | python json_flatten.py > output.json

where your_input.json is the input JSON file, and output.json is the new JSON file that will be created.

## Unit testing 
The unit test can be found in test_flatten.py, and can be run using:

python -m unittest test_flatten.py

