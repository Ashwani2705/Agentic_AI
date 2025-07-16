#Data Serialization 
import json
data={'name': 'John', 'age': 30, 'city': 'New York'}
#converting dictionary to JSON string
json_string=json.dumps(data)
print(json_string)
print(type(json_string))

#interacting with api 
json.loads(json_string)  #converting JSON string back to dictionary
#accessing data
print(json.loads(json_string)['name'])  # Output: John