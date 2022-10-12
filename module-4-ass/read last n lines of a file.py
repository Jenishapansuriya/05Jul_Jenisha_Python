f1 = "file.txt"
val = int(input("Enter some random number = "))
with open(f1, 'r') as filecontent:  
    lines_lst= filecontent.readlines()
    print("The last",val,"lines of a given file are:")
    for fline in (lines_lst[-val:]):
        print(fline, end ='')