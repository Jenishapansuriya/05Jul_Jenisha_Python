try:
    n = int(input(" Please Enter any Maximum Value : "))
    for number in range(1, n ):
         if(number % 2 != 0):
            print("{0}".format(number))
except Exception as error:
    print(error)