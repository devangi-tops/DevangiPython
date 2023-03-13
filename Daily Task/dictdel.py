#del: it can element from dictionry index vise also can delet whole the dict
d=dict(name="Devangi",age="26",DOB="19/12/1996",vehical="car")

del d['DOB']

print (d)

#.clear(): it will remove all the elements of the dictionary

d.clear()
print(d)

#Aplying list,tuple & diction as value inside  a dictionary

D={
    1:('O':"Orange",'A':"Apple"),

    2:("t1","t2"),
    'num':[1,2,3,4,5,6,7]
}

print("Accesss list element from dict : ",D['num'][4])
print("Access Tuple element from dict : ",D[2][4])
