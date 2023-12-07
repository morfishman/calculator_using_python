from calculator import *


def first_index(string : list,charecture :str)-> int:
    for char in range(len(string)):
        if string[char] == charecture: return char
    return -1

def input_check(expression :str) -> list:
    expression = expression.replace(' ','')
    laxers_array = []
    buffer = ''
    for laxer in expression:
        if laxer not in ['+','-','/','^','*']:
            buffer+=laxer
        elif buffer != '':
            if buffer.isdigit():
                laxers_array.append(buffer)
                buffer = ''
                laxers_array.append(laxer)
            else:
                print(f"in operand {buffer}\n", read_error_messages(file_path='Errors.json', error_type='input errors', where='operand'))
                return []
        else:
            print(f"in syntax {laxer}\n",read_error_messages(file_path='Errors.json', error_type='type errors', where='operator'))
            return []
    if buffer != '':
        if buffer.isdigit():
            laxers_array.append(buffer)
            buffer = ''
        else:
            print(f"in operand {buffer}\n",read_error_messages(file_path='Errors.json', error_type='input errors', where='operand'))
            return []
    if laxers_array == [] or laxers_array[len(laxers_array)-1] in ['+','-','/','^','*']:
        print(f"in syntax {laxer}\n",read_error_messages(file_path='Errors.json', error_type='input errors', where='operator'))
        return []
    return laxers_array

def calc_expreation(expression :list) -> float:
    if len(expression) == 1:
        return float(expression[0])
    else:
        pow_index = first_index(expression, '^')
        div_index = first_index(expression,'/')
        mul_index = first_index(expression,'*')
        add_index = first_index(expression,'+')
        sub_index = first_index(expression,'-')
        useble_index = None
        func = None
        if pow_index != -1:
            useble_index = pow_index
            func = pow
        elif mul_index != -1 and div_index  != -1:
            if mul_index> div_index:
                useble_index = div_index
                func = div
            else:
                useble_index = mul_index
                func = mul
        elif mul_index != -1 or div_index  != -1:
            if mul_index == -1:
                useble_index = div_index
                func = div
            else:
                useble_index = mul_index
                func = mul

        elif add_index != -1 and sub_index != -1:
            if add_index > sub_index:
                useble_index = sub_index
                func = sub
            else:
                useble_index = add_index
                func = add
        else:
            if add_index == -1:
                useble_index = sub_index
                func = sub
            else:
                useble_index = add_index
                func = add


        operator = expression.pop(useble_index)
        operand2 = expression.pop(useble_index)
        operand1 = expression[useble_index - 1]
        expression[useble_index - 1] = gerneral_aritmatic(operand1=float(operand1), operand2=float(operand2),operator=operator, function_aritmatic= func)
        if expression[useble_index - 1] == None:
            return

        return calc_expreation(expression)
