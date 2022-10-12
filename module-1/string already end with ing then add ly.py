x=input("enter a  string :-")
y=x[-3:]
if(x[-3:]=='ing'):
    y = x +'ly'
elif(len(y) <3):
    print(y)
else:
    y=x+'ing'
print(y)