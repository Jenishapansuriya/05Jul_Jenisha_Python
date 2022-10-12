my_string = input("Enter the string :")
list=[]
list=my_string.split()
word_freq=[list.count(p) for p in list]
print("The frequency of words is ...")
print(dict(zip(list,word_freq)))