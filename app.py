from string_interpeter import *

expression = input("[*]welcome to the bet calculator the world has to offer[*]\n~ write any expression that contains (+,-,*,^) and numbers \n~ calc: ")
if expression[0] == '-':
    expression = '0'+expression

laxical = input_check(expression)
while laxical != []:
    print(' = ',calc_expreation(laxical))
    expression = input(
        "\n~ calc: ")
    if expression[0] == '-':
        expression = '0' + expression
    laxical = input_check(expression)