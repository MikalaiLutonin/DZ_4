# Задача B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def encode_equation(equation: str) -> dict:                                   # функция преобразования из строки в словарь
    new_equation = []
    equation = equation.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').split(' ')
    for item in equation:
        if not 'x' in item:
            new_equation.append([item, 0])
        else:
            if item.endswith('x'):
                if item == 'x':
                    new_equation.append(['1', '1'])
                elif item == '-x':
                    new_equation.append(['-1', '1'])
                else:
                    new_equation.append((item + '1').split('*x'))
            else:
                if item.startswith('x'):                                            # если строка начинается с x, то ...
                    new_equation.append(('1' + item).split('x**'))
                elif item.startswith('-x'):
                    new_equation.append(item.replace('-', '-1').split('x**'))
                else:
                    new_equation.append(item.split('*x**'))
    equation_pattern = {}
    for item in new_equation:
        equation_pattern[int(item[1])] = int(item[0])
    return equation_pattern


file_first = open('first.txt', 'r')
for i in file_first:
    print('Первый многочлен: ')
    print(i)
    dict_first = encode_equation(i)
file_first.close()


file_second = open('second.txt', 'r')
for i in file_second:
    print('Второй многочлен: ')
    print(i)
    dict_second = encode_equation(i)
file_second.close()



def equation_addition(first: dict, second: dict) -> dict:
    base = {}
    base.update(first)
    base.update(second)
    for key in base:
        if first.get(key) and second.get(key):
            base[key] = first.get(key) + second.get(key)
        elif first.get(key):
            base[key] = first.get(key)
        else:
            base[key] = second.get(key)
    return dict(sorted(base.items())[::-1])

dict_result = equation_addition(dict_first, dict_second)


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

result = decode_equation(dict_result)



print('Сумма многочленов: ')
print(result) 






