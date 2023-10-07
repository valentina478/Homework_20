import seaborn
import matplotlib.pyplot as plt
import re


titanic_data = seaborn.load_dataset('titanic') #task_1
tips_data = seaborn.load_dataset('tips')

def task_2():
    seaborn.histplot(data=titanic_data['age'])
    plt.title('Розподіл по віку')
    plt.xlabel('Вік')
    plt.ylabel('Кількість')
    plt.show()
# task_2()

def task_3():
    seaborn.scatterplot(x=tips_data['total_bill'], y=tips_data['tip'], data=tips_data)
    plt.xlabel('Рахунок')
    plt.ylabel('Чайові')
    plt.show()
# task_3()

def task_4():
    print('Середнє значення', tips_data['total_bill'].mean())
    print('Медіана', tips_data['total_bill'].median())
    print('Дисперсія', tips_data['total_bill'].var())
# task_4()

def task_5():
    while True:
        try:
            user_input = input('Введіть ціле число: \n')
            number = int(user_input)
            break
        except ValueError:
            print('Помилка! Ви ввели не ціле число. Спробуйте ще раз.\n')
    print(f'Ви ввели ціле число: {number}. Дякуємо за співпрацю!' )
# task_5()

def task_6():  
    while True:
        user_input = input('Введіть свій вираз з двома значеннями: \n Для виходу — q \n')
        values = re.split(r'[+\-*/]', user_input)
        def action(action):
            if action == '+':
                result = int(values[0]) + int(values[1])
            elif action == '-':
                result = int(values[0]) - int(values[1])
            elif action == '*':
                result = int(values[0]) * int(values[1])
            elif action == '/':
                result = int(values[0]) / int(values[1])
            else:
                result = 'Невідомий оператор. Спробуйте ще раз'
            print(result)
        if user_input.lower() == 'q':
            print('Дякуємо за користування!')
            break
        else:
            try:
                for e in values:
                    number = int(e)
            except (ValueError, NameError) as er:
                print(er)
                print('Помилка! Ви ввели не коректне значення. Спробуйте ще раз.\n')
            else:
                for o in ['+', '-', '*', '/']:
                    if o in user_input:
                        action(o)
# task_6()