user_acct = ['yuxianan','fengshuo','yuzizhen','wangshuaiwen','admin']

for each_one in user_acct:
    if each_one == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello '+ each_one +',thank you for logging in again.')
