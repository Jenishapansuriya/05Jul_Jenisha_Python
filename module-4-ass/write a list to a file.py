mobile=['samsung','redmi','oneplus']

file=open('ff.txt','w')
for items in mobile:
    file.writelines([items])

file.close()