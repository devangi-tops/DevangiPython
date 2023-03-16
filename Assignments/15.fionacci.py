first=0
second=1
print(first)
print(second)
N=int(input('Upto which element : '))

for a in range(1,N):
    third=first+second
    print(third)
    first,second=second,third
