mylist=[]
n=int(input("Enter the number of element:"))
for i in range(n):
    ei=(input("Enter the list element:"))
    mylist.append(ei)
if not mylist:
    print("The List is Empty")
else:
    print("The List is Not Empty")

print(mylist)    