#1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
print('Введите построчно текст для записи в файл. Для окончания ввода введите пустую строку.')

input_str = None

with open('temp1.txt','w') as f_obj:
    while input_str != "":
        input_str = input('> ')
        f_obj.write(input_str+'\n')

#2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

num_str = 0
num_words = []

with open('temp2.txt','r') as f_obj:
    for line in f_obj:
        num_str += 1
        num_words.append(len(line.split(" ")))

print(f"В файле cтрок - {num_str}")
for i,val in enumerate(num_words):
    print(f"В строке {i+1} количество слов - {val}")

#3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

#Пример файла:

#Иванов 23543.12
#Петров 13749.32

employers = 0
sum_oklad = 0

print('Фамилии сотрудников с окладом менее 20 тысяч:')

with open('temp3.txt','r') as f_obj:
    for line in f_obj:
        surname, oklad = line.split(" ")
        if float(oklad) < 20000:
            print(surname)
        employers += 1
        sum_oklad += float(oklad)

print(f'Средний оклад сотрудников - {sum_oklad/employers:.2f}')
        

#4. Создать (не программно) текстовый файл со следующим содержимым:

#One — 1
#Two — 2
#Three — 3
#Four — 4
#Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

numbers = {
    'One' : 'Один',
    'Two' : 'Два',
    'Three' : 'Три',
    'Four' : 'Четыре'
    }

with open('temp4.txt','r') as f_obj_from:
    with open('temp4_new.txt','w') as f_obj_to:
        for line in f_obj_from:
            newline = line.replace(line.split(" ")[0], numbers[line.split(" ")[0]])
            f_obj_to.write(newline)


#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

sum = 0

with open('temp5.txt','w+') as f_obj:
    for i in range(10):
        f_obj.write(str(randint(0, 10))+" ")
    f_obj.seek(0)
    my_list = f_obj.read().split(" ")
    my_list = my_list[:-1]
    print(my_list)
    for i in my_list:
        sum += int(i)

print(f'Сумма числе в файле - {sum}')

#6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.

#Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_dict = {}

with open('temp6.txt','r') as f_obj:
    for line in f_obj:
        line = line.replace("\n","")
        my_list = line.split(" ")
        subj = my_list[0][:-1]
        hours = 0
        for i in range(1,4):
            if my_list[i] != "—":
                hours += int(my_list[i][0:my_list[i].index('(')])
        my_dict[subj] = hours

print(my_dict)


#7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.

#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.

#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).

#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.

#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджер контекста.

import json

firm_dict = {}
profit_dict = {}

profit_all = 0
profit_average = 0
firm_num = 0

with open('temp7.txt', 'r') as f_obj:
    for line in f_obj:
        firm_name, firm_form, income, cost = line.split()
        firm_dict[firm_name] = int(income) - int(cost)
        if firm_dict[firm_name] >= 0:
            profit_all += firm_dict[firm_name]
            firm_num += 1
    if firm_num > 0:
        profit_average = profit_all / firm_num
    else:
        print('Все компании работают в убыток')
    profit_dict = {'average_profit': profit_average}
    
my_json = []
my_json.append(firm_dict)
my_json.append(profit_dict)

print(my_json)


with open('temp7.json', 'w', encoding = 'utf-8') as f_json:
    json.dump(my_json, f_json, ensure_ascii=False)





