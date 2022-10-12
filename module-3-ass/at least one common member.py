
def commonelement(A, B): 
   c = "NOT FOUND"

   
   for i in A: 
      
      for j in B: 
         
         if i == j: 
            c="FOUND"
            return c  
    


A=list()
B=list()
n1=int(input("Enter the size of the first List ::"))
print("Enter the Element of first List ::")
for i in range(int(n1)):
   k=int(input(""))
   A.append(k)
n2=int(input("Enter the size of the second List ::"))
print("Enter the Element of second List ::")
for i in range(int(n2)):
   k=int(input(""))
   B.append(k)

print("Display Result ::",commonelement(A, B)) 