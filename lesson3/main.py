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

def my_print():
    a =7  # local var
    print('Hello')
    print('good day')

my_print()


# <editor-fold desc="Description">
def hello(name, age):
    print('Hallo')
# </editor-fold>


# region Description
hello('Dasha',8)
hello(input('Ent name:'), input('AGE'))
# endregion

def fuul_n (a, b, c):
    res = a + ' ' + b + ' ' + c
    return res


a1 = input('Name = ')
a2 = input('Family = ')
a3 = input('Age')

print(fuul_n(a1, a2, a3))


