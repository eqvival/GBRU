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

# комплексное число
a = complex(2,5)
print(a)
# ================================================================

name = 'Maria'
st = 'Hello how are you?'
print(st[2])
print(st[1])
print(st[-1])
print(st[0:4])
print(st[0:5])
print(st[7:])
print(st[0:10:2])
#переворот строки
print(st[::-1])
l = len(st)
print(l)
print(st[l-1])
res = st.split()
print(res)
res=st.split('o')
a = input('числа ').split()
print(a)
print(res)
res = ' '.join('helo', 'Mike')
print(res)
# посчитать число вхожждений
print(st.count('you'))
#замена
res = st.replace('o','BBB')
print(res)

#ans = input().lower()
#ans = input().upper()

# все заглавные
print(st.upper())

#Первая заглавная
print(st.capitalize())

#каждое слово после пробела с заглавной
print(st.title())
#


#for
st = 'helow, how are you'

for el in st:
    print(el)
#--------------------------

for i in range(0, len(st) - 1):
    print(st[i])
# range обрезает значение
for i in range(0, len(st)):
    print(st[i])


# списки
#
li = [2, 3, 4, 6, 7, 'Hello', 89.68, True, [12,5]]
print (li)
print (li[2])
print (li[1:3])
# поменять местами первый и последний
li[0], li[-1]=li[-1], li[0]
print (li)
# добавление нового элемента
li.append('new element')
print ('after',li)
#вставка элементов
li.insert(3, False)
# подсчет вхождений
print(li.count(True))
print('before', li)
li.remove('Hello')
print('after', li)

if el in li:
    li.remove(el)
print('after', li)

#
li = [2, 'Hello', 89.86, True, [12,5]]
for el in li:
    print(el)

for i in range(0, len(li)):
    print(li[i])



st = input('ENTER DATA: ').lower().split()
for word in st:
    print(word)
    if word[0] =='б':
        print(word)
# с нумерацией
li = [2, 'Hello', 89.86, True, [12,5]]
for i, el in enumerate(li,1): # указывается элемент и номер с которго идет нум-я
    #Если не указано с чего начинать - идет с 0
    print(f'{i}, {el}')


# кортеж  tuple неизменяемый список

cort = (2, 'Hello', 89.86, True, [12,5], (1, 2, 3))

# Словарь dict
di = {'Bob': 123, 'Nick': 876, 'Ann':678}
print(type(di))
print(di['Nick'])
print(di.get('Nick'))
di['Kate'] = 160
print(di.keys())
print(di.values())
print(di.items())

marks = {'otl': [10, 9, 8], 'chor':[7, 6], 'ud':[5, 4, 3], 'neud':[2, 1]}
n = int(input('Enter MARK'))
for el in marks:
    if n in marks[el]:
        print(el)
        break


