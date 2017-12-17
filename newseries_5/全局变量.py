

def new():
    a = 123
    def mod():
        nonlocal a
        a = a+110
        print(a)
    return mod()


new()
