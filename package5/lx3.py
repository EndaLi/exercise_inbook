user_acct = ['yuxianan','fengshuo','yuzizhen','wangshuaiwen','admin']
del user_acct[:]


if user_acct:
    for each_one in user_acct:
        print('Hello '+ each_one + ',thank you for logging in again.')
else:
    print('we need to find some users')
