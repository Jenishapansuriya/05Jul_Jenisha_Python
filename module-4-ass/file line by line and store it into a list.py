def file_read(n):
        with open(n) as f:     
                content_list = f.readlines()
                print(content_list)

file_read('file.txt')