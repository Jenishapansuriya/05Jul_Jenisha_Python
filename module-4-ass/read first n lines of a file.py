from itertools import islice
f1 = "file.txt"
val = int(input("Enter some random number = "))
with open(f1, 'r') as givenfilecontent:
  for f_line in islice(givenfilecontent, val):
     print(f_line)
