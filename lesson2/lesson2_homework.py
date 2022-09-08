# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


spisok = [1, 2, 4, 67, 89, 'дерево', 'дорога', True, False, [1,4]]
for elem in spisok:
    print(type(elem))

#
#
#2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
# и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно
# использовать функцию input()

spis = input('ENTER DATA: ').lower().split()
print('Before =', spis)
element = len(spis)
#print ('element = ', element)
if element % 2 != 0:
    for i in range(1,element, 2):
        spis[i-1], spis[i] = spis[i], spis[i - 1]
        #print('i= ',i)
else:
    for i in range(1, element, 2):
        spis[i - 1], spis[i] = spis[i], spis[i - 1]
        #print('i= ', i)
print('After', spis)


#
#

#. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и dict.

## list

month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# month_name=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'octb', 'nov', 'dec']
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
outmn = [9, 10, 11]
month_inp = int(input('INPUT MONTH = '))
for i in range(0, 3):
    #print('i= ', i)
    if month_inp == winter[i]:
        print('winter')
        #print(winter[i])
        #print('i= ', i)
        break
    elif month_inp == spring[i]:
        print('spring')
        #print(spring[i])
        #print('i= ', i)
        break
    elif month_inp == outmn[i]:
        print('Outmn')
        #print(outmn[i])
        #print('i= ', i)
        break
    elif month_inp == summer[i]:
        #print(summer[i])
        print('Summer')
        #rint('i= ', i)
        break
print('FINISH')


# DICT
month_inp = 0
month_slov = {'winter':[1, 2, 12], 'spring':[2, 4, 5], 'summer':[6, 7, 8], 'outmn':[9, 10, 11]}
month_inp = int(input('INPUT MONTH = '))
for elemm in month_slov:
    if month_inp in month_slov[elemm]:
        print(f'введенное значение = {month_inp} , найденое   = {month_slov[elemm]}')
        print(elemm)
        break


#Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки нужно
# пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

new_word = ''
my_words = input('ENTER DATA: ').split()
for word in my_words:
    if len(word) >= 10:
        for i in range(0, 10, 1):
            new_word = new_word + word[i]
            #print(f'now= {new_word} i= {i}')
        print(new_word)
        new_word = ''
        #break
        #print(len(word))
    else:
        print(word)


# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У пользователя
# нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
# элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

ffff = [2, 3, 8, 1, 1, 3, 4]
ffff.sort(reverse=True)

new_r = int(input('Рейтинг'))
#double_d = dounle digit если что )
double_d = ffff.count(new_r)
#print(double_d)
#print(len(ffff))
#print(ffff)
if double_d >= 1:
    for i_count in range(0, len(ffff)):
        #if i_count == ffff[i_count]:
        if new_r == ffff[i_count]:
            double_d = double_d - 1
            if double_d == 0:
                ffff.insert(i_count+1, new_r)
                break #if
else:
    if double_d == 0:
        for i_count in range(0, len(ffff)):
            if new_r > ffff[i_count]:
                ffff.insert(i_count, new_r)
                break #if

print(ffff)


# * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть
# характеристиками товара: название, цена, количество, единица измерения. Структуру нужно сформировать программно,
# запросив все данные у пользователя.
#Пример готовой структуры:

#[
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]

#Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название. Тогда значение — список значений-характеристик, например, список названий товаров.
#Пример:

#{
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#}
#Пока не сделал - если успею - сделаю обновлю

#

tovar = [(0,{'name': 'Название', 'cena': '0', 'colvo':0, 'edinicy':'шт'})]

poz = int(input('Введите кол-во позиций номенклатуры, которые хотите добавить = '))

for schtchk in range(1, poz):

    namet = input('Введите навзание номенклатурной единицы')
    cenat = input('Введите цену')
    colvot = input('Введите кол-во')
    edinicyt = input('Введите единицу измерение( штуки, кг) ')
    tovar.append([(schtchk, {'name': namet, 'cena': cenat, 'colvo':colvot, 'edinicy':edinicyt})])

print(tovar)

analitik_t = {'name':'', 'cena':0, 'colvo':0, 'edinicy':'' }

poz = len(tovar)
for schtchk in range(0,poz):
    analitik_t.keys('name') += tovar.count