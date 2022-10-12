sub = {'math':100,'Eng':100,'Chem':98,'students':['jack','mack']}
if all(key in sub for key in ('Eng','Chem')): 
    print("given all keys are present in dictionary") 
else: 
    print("given all keys are not present in dictionary")