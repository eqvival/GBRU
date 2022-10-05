###1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных будет свидетельствовать пустая строка.

my_fl = open('mytext.txt', 'a')
while True:
    strk = input('Строка')
    if len(strk) == strk.count(' '):
        my_fl.close()
        break
    else:
        my_fl.writelines(strk)


#2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
# строке.

my_fl2 = open('sample.txt', 'r')
stroka = 0
wrd = 0

for sttr in my_fl2:
    stroka = stroka + 1
    wrd = wrd + sttr.count(' ') + 1

print('Строк = ', stroka)
print('Слов = ', wrd)


#3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее
# 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить
# подсчёт средней величины дохода сотрудников.
#Пример файла:

#Иванов 23543.12
#Петров 13749.32

spr ={}
my_fl3 = open('oclad.txt', 'r')
itm = 0
sum_ocl = 0
strk = []
less20 = []
for stk in my_fl3:
    strk = stk.split()
    spr[strk[0]] = strk[1]
    itm = itm + 1 # считаю строки\позиции
    #print('itm = ', itm)
    #print('strk 0 = ', strk[0])
    #print('strk 0 = ', strk[1])
    sum_ocl = sum_ocl + int(strk[1])
    if int(strk[1]) < 20000:
        #stroka = strk[0] + ' '  + str[1] + ' '
        less20.append(strk[0])
sred = sum_ocl / itm
print('Средний доход = ', sred)
print('Человек = ', itm)
print('Доходы меньше 20000 имеют - ', less20)



#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

eng_wrd = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
rus_wrd = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять', 'Десять']
elem = 0

def GIVEMENUM(sample):
    for scht in range(0,len(eng_wrd)):
        if sample == eng_wrd[scht]:
            return scht


my_fl4 = open('chisl.txt', 'r')
my_fl5 = open('chisl_new.txt', 'w')
for stk in my_fl4:
    strk = stk.split()
    elem = GIVEMENUM(strk[0])
    new_str = rus_wrd[elem] + ' ' + strk[2]
    my_fl5.writelines(new_str)
    print('НОВАЯ СТРОКА = ', new_str)

my_fl5.close()
#print('START =====', my_fl4)
my_fl4.close()
#print('STOP', my_fl5)



#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить её на экран.


def m_summa(lineforsumm):
    summa = 0
    for i in lineforsumm:
        summa = summa + int(i)
        #print(summa)
    return summa

my_fl6 = open('digi.txt', 'w')
digits = [i for i in range(1, 50)]
print('Список чисел', digits)
for spl in range (0, len(digits)):
    wrstr = str(digits[spl]) + ' '
    #my_fl6.writelines(str(digits[spl] + ' ')
    my_fl6.write(wrstr)
my_fl6.close()
my_fl6 = open('digi.txt', 'r')

for stk in my_fl6:
    #print('STK = ', stk)
    strk = stk.split()
    #print ('STRK= ', strk)
    #print(type(strk))
    #print(m_summa(stk))
    summa_big = summa_big + m_summa(strk)

print(summa_big)



#6 (Дополнительно). Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
# scrach 56

def CLEAN_P(strk_n):
    result = ''
    sk_index = strk_n.find('(')
    print('SEND = ', strk_n)
    print('SK = ',sk_index)
    print ('SK type', type(sk_index))
    #result = strk_n[0, int(sk_index)]
    for i in range(0, sk_index):
        result = result + strk_n[i]

    print('result= ', result)
    return result


my_fl7 = open('uroki.txt', 'r')
predm = {}

for stk in my_fl7:
    stk = stk.replace('—', '')
    stk = stk.replace('-', '')
    strk = stk.split() #разделяем прочитанную строку
    wrd_count = len(strk)
    print(wrd_count)
    #for wrd in strk:
     #   if wrd.count('(') == 0:
      #      key_name = wrd.replace(':','')     #[0,len(wrd)]
       #     print('KEY NAME', key_name)
        #elif wrd.count('(') == 1:
         #   sk_index = wrd.find('(')
          #  wrd = wrd[0, sk_index]
        #if predm.values(key_name) == 0:
          #  predm[key_name] = int(wrd)
        #else:
         #   predm[key_name] = predm.values(key_name) + int(wrd)
       # print('values = ', predm.items(key_name))


    if wrd_count == 4: # передаем данные функции извлечения
       key_name = strk[0].replace(':', '')
       lessons_hours = int(CLEAN_P(strk[1])) + int(CLEAN_P(strk[2])) + int(CLEAN_P(strk[3]))
       predm[key_name] = lessons_hours
       print('KEy NAME 4= ', key_name)
       print('LESSON HOURS', lessons_hours)
    elif wrd_count == 3:  # передаем данные функции извлечения
        key_name = strk[0].replace(':', '')
        lessons_hours = int(CLEAN_P(strk[1])) + int(CLEAN_P(strk[2]))
        predm[key_name] = lessons_hours
        print('KEy NAME 3= ', key_name)
        print('LESSON HOURS 3', lessons_hours)
    elif wrd_count == 2:  # передаем данные функции извлечения
        key_name = strk[0].replace(':', '')
        lessons_hours = int(CLEAN_P(strk[1]))
        predm[key_name] = lessons_hours
        print('KEy NAME = ', key_name)
        print('LESSON HOURS', lessons_hours)
    elif wrd_count == 1:  # передаем данные функции извлечения
        key_name = strk[0].replace(':', '')
        lessons_hours = 0
        predm[key_name] = lessons_hours

        print('KEy NAME = ', key_name)
        print('LESSON HOURS', lessons_hours)

print(predm)



#7 (Дополнительно) . Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет
# содержать данные о фирме: название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.

#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]