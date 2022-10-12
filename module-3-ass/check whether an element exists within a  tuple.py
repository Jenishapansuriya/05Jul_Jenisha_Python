numTuple = (4, 6, 8, 11, 22, 43, 58, 99, 16)
print("Tuple Items = ", numTuple)

number = int(input("Enter Tuple Item to Find = "))

if number in numTuple:
    print(number, " is in the numTuple")
else:
    print(" We haven't found ", number, " in numTuple")