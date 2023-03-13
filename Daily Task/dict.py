d1={'k1':12,'k2':123,'msg':'Hello All'}

d2=dict(name="abc",name2="pqr",name3="jkl")

print(d1)
print(d2)

#dictionary acess

print(d1['k2'])

#.get() method:

print(d1.get('msg'))

#copy & update  Dictionary

dict1=d2.copy()

print("Dict : 1 copy from d2=",dict1)

dict1.update(d1)

print("Dict : 1 update from d1=",dict1)
