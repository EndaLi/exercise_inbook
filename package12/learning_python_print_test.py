filename = 'learning_python.txt'

with open(filename) as file_opening:
    lines = file_opening.readlines()

for line in lines:
    print(line.rstrip())
