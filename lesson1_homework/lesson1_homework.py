# 1 задание урока
digit1 = 0
digit2 = 0
digit1 = int(input('input gigit1'))
digit2 = int(input('input gigit2'))
ask = input('Что мы будем делать?')
result = 0
if ask == '+':
    result = digit1 + digit2
    print('Сложение, а сумма =', result)
    print(f'1={digit1} 2={digit2}')
elif ask == '*':
    result = digit1 * digit2
    print('Умножение, а результат =', result)
    print(f'1={digit1} 2={digit2}')
elif ask == '/':
    result = digit1 / digit2
    print('Деление, а результат =', result)
    print(f'1={digit1} 2={digit2}')
elif ask == '-':
    result = digit1 - digit2
    print('Вычитание, а результат =', result)
    print(f'1 {digit1} 2={digit2}')
else:
    print(f'Сначала ты ввел {digit1} , потом {digit2}, ответил {ask} . {ask} , Карл? поробуй еще!')



# 2
sec_inp = 0
min_res = 0
hours_res = 0
sec_res = 0
sec_inp = int(input('sec= '))

if (sec_inp % 3600) == 0:
    min_res = sec_inp // 60
    hours_res = min_res // 60
    print(f'В {sec_inp} sec {min_res} min , {hours_res} hours')
    print(int(hours_res), ':',int((sec_inp)-hours_res*3600) // 60), 'min ',':',int(sec_inp - (sec_inp - hours_res*3600) // 60)
else:
    hours_res = sec_inp // 3600
    min_res = (sec_inp - hours_res * 3600) // 60
    if  (sec_inp - hours_res * 3600) % 60 != 0:
        sec_res = sec_inp - hours_res*3600 -min_res*60
        print(f'В {sec_inp} sec {min_res} min , {hours_res} hours')
        print(f'{hours_res}:{min_res}:{sec_res}')
    else:
        print(f'В {sec_inp} sec {min_res} min , {hours_res} hours')
        print(f'{hours_res}:{min_res}:{sec_res}')
        #print('Something going wrong')
#print


#3 Задание

digit1 = 0
digit2 = 0
digit3 = 0
result = 0
digit1 = input('INPUT CIFIR') # 333 дает забавный результат
digit2 = digit1 + digit1
digit3 = digit2 + digit1
print (f'1= {digit1} 2={digit2}  3= {digit3} ')
result = int(digit1) + int(digit2) + int(digit3)
print('Result =', result)

#4 задание (Поиск максимальной цифры)

digit1 = 0
digit2 = 0
digital_max = 0
digit1 = int(input('Input 1234567'))
while digit1 != 0:
    digit2 = digit1 % 10
    print('Digit2 = ', digit2)
    digit1 = digit1 // 10
    print('Digit1 = ',digit1)
    if digit2 > digital_max:
        digital_max = digit2
    else:
        print('xxxxxxxxxxxxxxx')
print('MAXIMUM DIGIT',digital_max)



#5 Задание - прибыль\издержки

profit = 0
izdergki = 0
dohod = 0
profit = float(input('Выручка = '))
izdergki = float(input('Издержки = '))
if profit > izdergki:
    dohod = profit - izdergki
    print('all right! ', dohod)
elif profit == izdergki:
    print('Работа в 0')
else:
    print('Работа в убыток = ', profit - izdergki)


#6
profit = 0
izdergki = 0
dohod = 0
rentab = 0
workers = 0
profit = float(input('Выручка = '))
izdergki = float(input('Издержки = '))
workers = int(input('кол-во рабочих'))

if profit > izdergki:
    dohod = profit - izdergki
    print('all right! ', dohod)
elif profit == izdergki:
    print('Работа в 0')
else:
    print('Работа в убыток = ', profit - izdergki)

rentab = ((profit - izdergki) / profit) * 100
workers = (profit - izdergki) / workers # исползую переменную т.к. она уже не нужна
print('Рентабильность = ', rentab)
print('Доход на сотрудника',workers)


#7

a = 0
a_day = 0
b = 0
i = 0
a = float(input ('Стартовая дистанция = '))
b = float(input ('Нужно достигнуть = '))
while a_day != b:
    a_day = a_day + a * 0.1
    i += 1
    print (f'результат {i} дня {a_day} км')
    print('*'*30)
print('Результат будет достигнут на, день ', i)