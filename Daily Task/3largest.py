#WAP to find the highest 3 values in a dictionary
import nlargest
my_dict = {'a':400,'b':200,'c':800,'d':100,'e':200}
three_largest =  nlargest(3, my_dict, key=my_dict.get)
print(three_largest)
