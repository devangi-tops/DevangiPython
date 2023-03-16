#WAP to find the highest 3 values in a dictionary

fruits = {"strawerry": 20,"apple": 300,"banana": 50,"papaya": 40,"mango": 65}

costly_fruits = sorted(fruits, key=fruits.get, reverse=True)

for index in range(3):
    print(costly_fruits[index])

