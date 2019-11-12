# Товары. Задание 6 + 7
# Указываем стартовые переменные
a = []
counter = 0

# Функция для вывода сохраненных значений
def check_data():
    print('Стандартный вывод:')
    print(a)
    print('Вывод с форматированием:')
    print('\n'.join('{}: {}'.format(*k) for k in a))
# Функция для анализа данных (7 задание)
def analyze():
    naming = []
    costing = []
    counting = []
    evaluating = []
    for i in range(len(a)):
        naming.append(a[i][1]['Название'])
        costing.append(a[i][1]['Цена'])
        counting.append(a[i][1]['Количество'])
        evaluating.append(a[i][1]['Ед'])
    analitics = dict(Название=naming, Цена=costing, количество=counting, ед=evaluating)
    print(analitics)

# Функция для возможности выбора
def again():
    print('=== Для продолжения введите цифру === \n1)Добавить еще запись в бд:(1)\n2)Вывести данные и завершить:(2)\n3)Проанализировать данные:(3)')
    confirm = str(input())
    if confirm == '1':
        rem() # повторный вызов функции ввода, для добавления данных в бд
    elif confirm == '2':
        check_data() # вывод информации из бд
        return
    elif confirm == '3':
        analyze() # вызов функции анализа, которая переформатирует данные
        return
    else:
        print('Неверный параметр, введите цифру от 1 до 3')
        again()



# Основная функция для ввода данных и вызова обработчика
def rem():
    print('Введите название товара')
    name = str(input())
    print('Введите стоимость')
    try:
        price = int(input())
    except ValueError:
        print('Введите стоимость')
        price = int(input())
    print('Введите количество')
    try:
        count = int(input())
    except:
        print('Введите количество')
        count = int(input())
    print('Введите единицу измерения')
    ext = str(input())
    c = dict(Название=name, Цена=price, Количество=count, Ед=ext) # здесь формируется словарь
    global counter # для счетчика указывается что переменная глобальная
    counter += 1
    b = (counter, c) # формируется кортеж
    a.append(b) # формируется финальный список
    again()
rem() # вызов основной функции, фактический старт выполнения