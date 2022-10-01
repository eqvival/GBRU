# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#import math
#import time

#print(math.cos(12))
#time.sleep(2)
#print(math.sqrt(99))

from math import sin, sqrt, pi  #импорт контретных функций
import time as tme

#print(sin(65))
#print(sqrt(121))
#print(tme.time())
##
#from liba import my_func #импортируется файл my_func
#from liba.my_func import my_func import password, hello  #(password - переменная, hello - фугкция)


from sys import argv

print(argv)


from sys import argv

print(argv)
print(argv[1], argv[2], argv[3])
path, ar1, ar2, ar3 = argv


p1, p2, p3 = map(int,argv[1:])
print(type(p1))



