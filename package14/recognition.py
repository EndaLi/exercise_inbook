
def recognition(filename):
    try:
        with open(filename) as open_file:
            contents = open_file.read()
    except FileNotFoundError:
        #print("\n傻瓜，文件%s不存在！"% filename)
        pass
    else:
        print("\n这是我家的小宝宝：")
        each_word = contents.split()
        for word in each_word:
            print(word.replace("，","\n"))

filename = ('cats.txt','dogs.txt')
for each in filename:
    recognition(each)
