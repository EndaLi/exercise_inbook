'''
def creat_guestlog():
    filename = 'guest_book.txt'
    with open(filename,'a') as file_creat:
        file_creat.write(log_print_result)

while True:
    file_log = 'guest.txt'
    with open(file_log,'a') as file_sight_in:
        guest_name = input("请输入您的用户名：")
        file_sight_in.write("\n"+guest_name)
        print("Hello %s ！" % guest_name)
        log_print_result = "Hello "+guest_name+" !"
        creat_guestlog()
'''        

class New_user:
    pass
