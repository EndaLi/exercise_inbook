'''cars = input("what car do you want？")
print("Let me see if I can find you a Subaru.")
'''

'''mop = input("请问您有多少人用餐？ ")
mop = int(mop)

if mop >= 8:
    print("已经没有空桌了。")
else:
    print("有桌，请用XXX号桌。")
'''

while 1:
    num_0 = input("请输入一个数字让我猜猜是否是10的整数倍？")
    num_0 = int(num_0)

    if num_0 % 10 == 0:
        print("是10的整数倍！")
    else:
        print("不是10的整数倍！")
