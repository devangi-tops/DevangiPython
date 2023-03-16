def uniqueList(dat1):
    x = []
    for p in dat1:
        if p not in x:
           x.append(p)
    return x
dataList=[]
n=int(input("Enter total elements in a list"))
for k in range(n):
    dat=int(input("Enter in data list: "))
    datalist.append(dat)

print("Original List",dataList)
print(uniqueList(datalist))
