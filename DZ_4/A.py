# Задача A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



from random import randint as RI

def create_pattern(min: int, max: int) -> dict:              # функция создания словаря на k элементов, с рандомными значениями в min-max диапазоне 
    k = int(input('Задайте степень многочлена: '))
    equation_pattern = {}                                    # создаем словарь
    for key in range(k, -1, -1):                             # Ранжируем в обратном порядке от заданного числа [k до -1) с шагом -1
        value = RI(min, max)                                 # генерим рандомное число
        equation_pattern[key] = value                        # заполняем словарь
    return equation_pattern


def decode_equation(equation: dict) -> str:                  # функция создания строкового уравнения из словаря
    new_equation = ''                                        # объявляем новую строку
    first = True
    for (key, value) in equation.items():
        if value != 0:
            if first:
                if value > 0:
                    new_equation += f'{value}*x**{key} '
                else:
                    new_equation += f'-{value * (-1)}*x**{key} '
                first = False
            else:
                if value == 1:                                                # если значение = 1
                    if key == 1:
                        new_equation += f'+ x '
                    elif key == 0:
                        new_equation += f'+ 1 '
                    else:
                        new_equation += f'+ x**{key} '
                elif value > 1:                                               # если значение > 1
                    if key == 1:
                        new_equation += f'+ {value}*x '
                    elif key == 0:
                        new_equation += f'+ {value} '
                    else:
                        new_equation += f'+ {value}*x**{key} '
                elif value == -1:                                             # если значение = -1
                    if key == 1:
                        new_equation += f'- x '
                    elif key == 0:
                        new_equation += f'- 1 '
                    else:
                        new_equation += f'- x**{key} '
                elif value < 1:                                                # если значение < 1
                    if key == 1:
                        new_equation += f'- {abs(value)}*x '                    # значение по модулю
                    elif key == 0:
                        new_equation += f'- {abs(value)} '
                    else:
                        new_equation += f'- {abs(value)}*x**{key} '
    new_equation += '= 0'                                                       # добавили на конце = 0           
    return new_equation



first = create_pattern(-100, 100)
second = create_pattern(-100, 100)


print(decode_equation(first))
print(decode_equation(second))



with open('first.txt', 'w') as data:   # открыли файл в режиме перезаписи и назвали все это сокращенно data
    data.write(decode_equation(first))  

with open('second.txt', 'w') as data:   # открыли файл в режиме перезаписи и назвали все это сокращенно data
    data.write(decode_equation(second))  


