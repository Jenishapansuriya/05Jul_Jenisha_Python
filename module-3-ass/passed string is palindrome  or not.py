str=input("Enter a string:")
a=""
for element in str[::-1]:
    a = a+element

if (str==a):
    print(str, 'is a Palindrome string')
else:
    print(str,' is NOT a Palindrome string')