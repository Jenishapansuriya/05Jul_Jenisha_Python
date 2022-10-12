def file_read(n):
        with open (n, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('text.txt')