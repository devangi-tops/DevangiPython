#WAP to get the unique values from a list

list = [5,15,25,35,15,25,95,65,5]
unique_list=[]
for a in list:
    if a not in unique_list:
        unique_list.append(a)
        
print(unique_list)
