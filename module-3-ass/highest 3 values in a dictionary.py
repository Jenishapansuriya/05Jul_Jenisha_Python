from collections import Counter

my_dict = {'A': 50, 'B': 22, 'C': 56,'D': 20, 'E': 32, 'F': 99}
k = Counter(my_dict)

high_value = k.most_common(3)
print("Dictionary with 3 highest values:")
print("Keys : Values")
for i in high_value:
   print(i[0]," : ",i[1]," ")