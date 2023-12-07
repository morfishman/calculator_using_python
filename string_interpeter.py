from calculator import read_error_messages

def input_check(expression :str) -> bool:
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
                print(f"in operand {buffer}\n", read_error_messages(file_path='', error_type='input errors', where='operand'))
                return False
        else:
            print(f"in syntax {laxer}\n",read_error_messages(file_path='Errors.json', error_type='type errors', where='operator'))
            return False
    if buffer != '':
        if buffer.isdigit():
            laxers_array.append(buffer)
            buffer = ''
        else:
            print(f"in operand {buffer}\n",read_error_messages(file_path='Errors.json', error_type='input errors', where='operand'))
            return False
    if laxers_array == [] or laxers_array[len(laxers_array)-1] in ['+','-','/','^','*']:
        print(f"in syntax {laxer}\n",read_error_messages(file_path='Errors.json', error_type='input errors', where='operator'))
        return False
    return True






