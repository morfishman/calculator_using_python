from string_interpeter import *

expression = input("[*]welcome to the bet calculator the world has to offer[*]\n~ write any expression that contains (+,-,*,^) , numbers , white spaces \n~ calc: ")

laxical = input_check(expression)
while laxical != []:
    print(' = ',calc_expreation(laxical))
    expression = input(
        "\n~ calc: ")
    laxical = input_check(expression)

print("----thanks----")