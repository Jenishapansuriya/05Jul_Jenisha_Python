lst = eval (input("Enter a list :-"))

for i in lst:
    if lst.count(i) == 1 :
        print(i)