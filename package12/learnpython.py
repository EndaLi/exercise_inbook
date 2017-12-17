filename = 'learning_python.txt'

with open(filename) as file_replace:
    lines = file_replace.readlines()
    
for line in lines:
    new_line = line.replace('python','java')
    print(new_line.rstrip())
