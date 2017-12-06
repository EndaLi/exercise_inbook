while True:
    age = int(input("请输入您的年龄："))

    if age < 2:
        print("你的一个小baby")
    elif age >= 2 and age < 4:
        print("你正在蹒跚学步！")
    elif age >= 4 and age < 13:
        print("你是个儿童！")
    elif age >= 13 and age<20:
        print("你是青少年！")
    elif age >= 20 and age<65:
        print("你是成年人！")
    elif age >= 65:
        print("你是老年人！")
