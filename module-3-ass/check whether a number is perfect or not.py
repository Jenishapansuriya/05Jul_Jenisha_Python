

num = int(input("Enter a number :: "))
sumOfFactors = 0


for i in range(1,num):
    if num%i == 0:
        sumOfFactors += i;

if sumOfFactors == num:
    print(num ," is Perfect Number")
else:
    print(num ,"is not a Perfect Number")