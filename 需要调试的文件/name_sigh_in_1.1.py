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


file_name = 'guest_book.txt'
file_log = 'guest.txt'
file_cause = 'guestcause.txt'


def creat_file_guest():
    with open(file_log,'a') as file_log_0:
        file_log_0.write(guest_name)


def creat_file_guest_book():
    with open(file_name,'a') as file_log_1:
        file_log_1.write(guest_name_print)

def user_enquire():
    guest_enquire
    with open(file_cause,'a') as file_log_2:
        file_log_2.write(guest_enquire)

while True:
    guest_name = input("请输入您的用户名：")
    guest_name_print = "Hello %s ！" % guest_name
    print(guest_name_print)
    guest_enquire = input( guest_name + ",你为什么喜欢编程？")

    creat_file_guest()
    creat_file_guest_book()
    user_enquire()
    
