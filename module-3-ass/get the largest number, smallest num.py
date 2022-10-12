


NumList = []

j1 = int(input("Enter the Total Number of  Elements: "))
for i in range(1, j1 + 1):
    value = int(input("Enter the Value of %d Element: " %i))
    NumList.append(value)
print("\nList: ",NumList)

print("\nThe Smallest Element in this List is: ", min(NumList))
print("The Largest Element in this List is: ", max(NumList))