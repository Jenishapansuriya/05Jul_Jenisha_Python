with open("aaa.txt") as f:
    with open("copy.txt", "w") as f1:
        for line in f:
            f1.write(line)