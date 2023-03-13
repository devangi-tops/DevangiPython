#Housie Game
import random
L1 = []
for i in range(1,13):
    n = int(input("Enter Num: "))
    L1.append(n)
print(L1)

L2 = L1[:len(L1)//2]
L3 = L1[len(L1)//2:]

 for i in range(1,13):
     num=random.choice(L1)


     print("User1:",L2)
     print("User2:",l3)

     print("Lucky Number is:",num)
     
     if num in L2:
         L2.remove(num)
     else:
         L3.remove(num)


     if len(12)==0:
         print("==========User1 win the Game==========")
         break
     elif len(L3)==0:
         print("==========User2 win the Game==========")
         break


     L1.remove(num)
