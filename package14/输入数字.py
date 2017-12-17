def add_method():

    prompt_0 = input("请输入第一个数字：")
    prompt_1 = input("请输入第二个数字：")

    try:
        result = int(prompt_0+prompt_1)
    except ValueError:
        print("请输入一个整数！")
    else:
        print(result)

while True:
    add_method()
