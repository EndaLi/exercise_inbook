import json

json_file = 'favorite_num.json'
try:
    with open(json_file) as open_file:
        number = json.load(open_file)
except FileNotFoundError:
    ilike_num = input("what's your favorite num? ")
    with open(json_file,'w') as open_file:
        json.dump(ilike_num,open_file)
else:
    print("I know your favorite number!It's %s." % number)
