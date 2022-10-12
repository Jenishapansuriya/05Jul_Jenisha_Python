
n1=int(input("Enter the First No:"))
n2=int(input("Enter the two No:"))
n3=int(input("Enter the three No:"))

sum=n1+n2+n3
if n1==n2 or n2==n3 or n1==n3:
    print("Sum is zero")
else:
    print("Sum is:",sum)       
