cars = ['奥迪','奥拓','宝马','奔驰','吉利帝豪']



while True:
    car_name = input("请输入你喜欢的车品牌：")
    if car_name == '中华':
        print('很好测试成功Ture')
        break
    elif car_name in cars:
        print('很好回答正确！')
        break
    else:
        print("输入有误，请重新输入！")
        


