def file_read(n):
        from itertools import islice
        with open(n, "w") as myfile:
                myfile.write("hello Python \n")
                myfile.write("helo Java ")
        txt = open(n)
        print(txt.read())
file_read('aaa.txt')