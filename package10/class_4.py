class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name.title()+" "+ self.last_name.title()
        
        
    def describe_user(self):
        print("\nThe following is the account name for the application ：")
        print("\t"+  self.full_name)

    def greet_user(self):
        print("\tHello！ "+  self.full_name +"。")


class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileages = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ["can add post","can delete post","can ban user"]

    def show_privileges(self):
        print("\nAdministrator rights:")
        for each_privilege in self.privileges:
            print(each_privilege)



new_admin = Admin("Tomas","Wang")
new_admin.describe_user()
new_admin.greet_user()
new_admin.privileages.show_privileges()






