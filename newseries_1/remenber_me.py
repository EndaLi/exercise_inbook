import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("Waht's your name? ")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username.title(),f_obj)
        print("We'll remember you when you come back, "+username.title()+'!')
    return username

def chioce_faction():
    username = get_stored_username()
    while True:
        chioce = input("\"%s\" is your username?" % username)
        if chioce.lower() == 'yes':
            print("Welcom back, "+ username +'!')
            break

        elif chioce.lower() == 'no':
            username = get_new_username()
            break
                    
        else:
            print("输入有误，请重输！")
            continue

def greet_user():
    username = get_stored_username()
    if username:
        chioce_faction()
    else:
        get_new_username()



greet_user()
