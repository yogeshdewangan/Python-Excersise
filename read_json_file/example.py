import json

json.loads({"name":"yogesh"})  ## loads json which is in string format

json.load(open("txt.json", "r")) ## read from file



python_dict = {
    "username": "jiangnanmax",
    "age": 21
}

print(json.dumps(python_dict))



#####################################################

file = open("json.txt", "w")
print(type(file))

json.dump(python_dict, file)
file.close()