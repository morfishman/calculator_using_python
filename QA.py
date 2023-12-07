from string_interpeter import input_check, calc_expreation

def test_calculator(expression):
    laxical = input_check(expression)
    if laxical != []:
        result = calc_expreation(laxical)
        return result
    return None

# Test valid expressions
expression1 = "2 + 3 * 4"
result1 = test_calculator(expression1)
print(f"{expression1} = {result1}")

expression2 = "5 - 2 ^ 3"
result2 = test_calculator(expression2)
print(f"{expression2} = {result2}")

# Test invalid expressions
expression3 = "10 / 0"
try:
    result3 = test_calculator(expression3)
    print(f"{expression3} = {result3}")
except Exception as e:
    print(f"Error for expression '{expression3}': {str(e)}")

expression4 = "3 + abc"
try:
    result4 = test_calculator(expression4)
    print(f"{expression4} = {result4}")
except Exception as e:
    print(f"Error for expression '{expression4}': {str(e)}")

# Add more test cases as needed
