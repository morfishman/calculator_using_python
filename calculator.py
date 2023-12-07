import json


def add(operand1: float, operand2: float) -> float:
    return operand1 + operand2

def sub(operand1: float, operand2: float) -> float:
    return operand1 - operand2

def mul(operand1: float, operand2: float) -> float:
    return operand1 * operand2

def div(operand1: float, operand2: float) -> float:
    return operand1 / operand2

def pow(operand1: float, operand2: float) -> float:
    return operand1 ** operand2

def read_error_messages(file_path,error_type,where):
    try:
        with open(file_path, 'r') as file:
            error_data = json.load(file)
            return error_data.get(error_type)[where]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None



def gerneral_aritmatic(operand1: float, operand2: float, function_aritmatic: object, operator: str) -> float:
    if type(operand2) == type(operand2) == float:
        return str(function_aritmatic(operand1,operand2))
    operand1_str = "\nerror in operand 1:" + str(operand1)
    operand2_str = "\nerror in  operand 2:" + str(operand2)
    error = read_error_messages(file_path='Errors.json',error_type="type errors", where=operator)
    buffer = error +\
             f"{operand1_str if not isinstance(operand1, float) else ''}\
               {(operand2_str if not isinstance(operand2, float) else '')}"
    print(buffer)
    return None




