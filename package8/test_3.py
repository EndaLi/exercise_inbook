responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == "no":
        polling_active = False
    elif repeat.lower() == "yes":
        continue
    else:
        polling_active = False

print("\n--- Poll Results ---")

for name,response in responses.items():
    print(name + " would like to climb " + response + '.')
