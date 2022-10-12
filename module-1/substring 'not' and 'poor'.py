s1 = input('Enter a string ')
s2=s1
c=d=0
c = s1.find('not')
d = s1.find('poor')
print(c,d)
if(c>=0 and d>=0):
    s2 = s2.replace(s2[c:d+4],'good')
print(s2)
