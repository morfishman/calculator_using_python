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
    except:
        print(f"Error: erorr not found at {error_type} -> {where}")
        return None


