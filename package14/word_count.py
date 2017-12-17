def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        #msg = "sorry,the file " + filename + " does not exist."
        #print(msg)
    else:
        words = contents.split()
        word_str = ''
        word_name = 'the'
        for each_word in words:
            word_str += each_word
        num_words = len(words)
        print("\nThe file %s has about %d words." %(filename,num_words))
        count_words = word_str.lower().count(word_name)
        print("The file has %d \"%s\"" % (count_words,word_name))

    

filename ='moby_dick.txt'
count_words(filename)


            
