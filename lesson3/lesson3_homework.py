### 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def zero_check(cifer):
    if cifer == 0:
        result = True
    else:
        result = False

    return result

def dolya (arg_1, arg_2):
    if zero_check(arg_2) == True:
        print(f'Введенный Элемент недопустим нужно ввести чило отличное от 0')
        while zero_check(arg_2) == True:
            #arg_1 = int(input('Введите делимое -'))
            arg_2 = int(input('Введите делитель ='))
        result = arg_1 / arg_2
        return result
    else:
        result = arg_1 / arg_2
        return result

arg_1 = int(input('Введите делимое -'))
arg_2 = int(input('Введите делитель ='))
print(dolya(arg_1,arg_2))

#2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год
# рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить
# вывод данных о пользователе одной строкой.

def namig_m(Namw, Fam, BDY, City, Nmail, Phn):
    print(f'ФИО {Namw} {Fam} год родения {BDY} город проживания {City}, электронная почта {Nmail} , телефон {Phn}')
    return True

NName = input('Name = ')
Fam = input('Family = ')
BDY = input('Birrthday Year')
City = input('City = ')
Nmail = input ('E-MALE = ')
Phn = input('phone nomber')

namig_m(Namw=NName, Fam=Fam, BDY=BDY, City=City, Nmail=Nmail, Phn=Phn)

#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
# аргументов.

def my_func (ar_1, ar_2, ar_3):
    if ar_1 >= ar_2 and ar_2 > ar_3:
        result = sum(ar_1, ar_2)
        return result
    elif ar_1 < ar_2 and ar_2 >= ar_3:
        result = sum(ar_2, ar_3)
        return  result
    else:
        result = sum(ar_1, ar_3)
        return result

arg_1 = input('digit 1 = ')
arg_2 = input('digit 2 = ')
arg_3 = input('digit 3 = ')

print(my_func(arg_1, arg_2, arg_3))

#4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение числа x
# в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной
# функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй —
# более сложная реализация без оператора **, предусматривающая использование цикла.

x = 0
y = 0
def my_func1(x,y):
    result = x ** y
    return result

def my_func2(x, y):
    result = 1
    for sch in range(0,abs(y)):
        result = result * x
        #print(result)
    result = 1 / result
    return result

x = int(input('1 ====== '))
y = int(input('2 ==== ')) * (-1)

print(my_func1(x,y))
print(my_func2(x,y))



#5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введён
# после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.


# <editor-fold desc="Description">
#result = 0
#spisok =['0', '0']
#while True:
#    spis = input('введите числа').split()

#    for scht in range(0,len(spis)):
#        if spis[scht] == 'stop':
#            print(f'1  {scht}  --  {spis[scht]}')
#            break

#        else:
#            spisok.append(spis[scht])
#            print(spis[scht])
#            print(type(spis[scht]))
#            result = result + int(spisok[scht])
#            print(f'res cycl {result}')
#    break
#    print(f'-{result}----{scht}----{spis[scht]}------------------------')
#print(f'RES {result}')
#print(spisok)
# </editor-fold>
# рабочий вариант

def summa_cif(cifry):
    result = 0
    i = len(cifry)
    for schet in range(0,i,1):
        if cifry[schet] == 'stop':
            return schet
        else:
            result = result + int(cifry[schet])

    return result

summa1 = 0
while True:
    spis = input('введите числа').split()
    summa1 = summa1 + summa_cif(spis)
    print(summa1)
    if spis.count('stop') >= 1:
        break


#6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.
#cap = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']
#low = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'й', 'к', 'л', 'м', 'н', '0', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ч', 'ш', 'щ', 'э', 'ю', 'я']
def int_func(stroka):
    cap = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
           'С', 'Т', 'У', 'Ф', 'Х', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']
    low = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'й', 'к', 'л', 'м', 'н', '0', 'п', 'р',
           'с', 'т', 'у', 'ф', 'х', 'ч', 'ш', 'щ', 'э', 'ю', 'я']

    for bukva in range(0, len(low)):
        #print('START I', bukva)
        #print('старт цикла', stroka[0])
        #print(bukva)
        if stroka[0] == low[bukva]:
            #print('stroka0 if', stroka[0])
            #print('LOW', low[bukva])
            stroka = stroka.replace(stroka[0],cap[bukva],1)
            #stroka.count = cap[bukva]
            #stroka = stroka.insert(stroka, low[bukva],cap[bukva])
            #print(f'First = {stroka[0]}  , Big = {cap[bukva]}')
            return stroka
        else:
            if stroka[0] == cap[bukva]:
                stroka = stroka
                #print(f'First = {stroka[0]}  , Big = BIG')
            return stroka

    return stroka

word = input('INPUT WORD >>>>>')
resultat = int_func(word)
print ('WORD', word)
print('resultat', resultat);


#7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Используйте написанную ранее функцию int_func().
###

#stroka = ' '
#vvod = input('введи слова в латинской раскладке').lower().split()

#def glav_func(slova):
    stroka = ''
    for cikl in range(0, len(slova), 1):

        #print('длинна slova= ',len(slova))
        #print('cikl----1= ', cikl)

        kusok = slova[cikl].capitalize()

        #print('cikl----2= ', cikl)
        #print('kusok', kusok)
        #print('stroka перед kusok =', stroka)

        stroka = stroka + ' ' + kusok
        #print('cikl----3= ', cikl)
        #print('cikl stroka - ', stroka)

    return stroka


print('получилось', glav_func(vvod))
#print('Введено = ',vvod)