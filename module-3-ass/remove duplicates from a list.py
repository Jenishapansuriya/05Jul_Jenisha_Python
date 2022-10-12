


dupList = []

ln = int(input("Enter the Total List of Items = "))
for i in range(1, ln + 1):
    listValue = int(input("Enter the %d List Item = " %i))
    dupList.append(listValue)

print("List Items = ", dupList)

uniqList = []

for val in dupList:
    if val not in uniqList:
        uniqList.append(val)
   
print("List Items after removing Duplicates = ", uniqList)