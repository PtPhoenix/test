from tkinter import W


word_list=[]
prefix = input("Prefix: ")
i = 0
result = []
result.append(prefix)
while i<3:
    word = input("Add a word: ")
    word_list.append(word)
    with_prefix = prefix + word
    result.append(with_prefix)
    i+=1
print(result)