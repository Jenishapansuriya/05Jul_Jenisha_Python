myDict = {'a': 'apple', 'b': 'Banana' , 'o': 'Orange', 'm': 'Mango','w':'watermelon'}
print("Dictionary : ", myDict)

k = input("Please enter the Key you want to search for: ")
if k in myDict.keys():
    print("\nKey Exists in this Dictionary")
    print("Key = ", k, " and Value = ", myDict[k])
else:
    print("\nKey Does not Exists in this Dictionary")