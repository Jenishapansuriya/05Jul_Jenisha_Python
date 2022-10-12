d1={"Name":"krishna" , "Age":22}
d2={"City": "Rajkot", "Gender": "Male"}
d3={"Mark":500}
d4 = {}
for d in (d1, d2, d3): d4.update(d)
print(d4)