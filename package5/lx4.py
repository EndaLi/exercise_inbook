current_users = ['yuxianan','fengshuo','yuzizhen','wangshuaiwen','admin']
new_users = ['betta','lilian','Yuzizhen','Wangshuaiwen','yolanda']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user.lower() + "已经存在，需要重新输入新的用户名！")
    else:
        print(new_user.lower() +"未被使用，可以注册！")
