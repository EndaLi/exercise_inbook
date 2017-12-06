car = input(str("请输入车名："))

if car.lower() == 'subaru' or car.lower() == 'audi':
    print("Is car == '%s' I predict True." % car)
    if car.lower() == 'subaru':
        print("I like it!")
else:
    print("I predict False.")
    
