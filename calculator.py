first= input('enter your first number : ')
operator = input('enter Operator (+,-.*./,%): ')
second= input('enter your second number : ')

first= int(first)
second= int(second)

if  operator == '+':
    print (first + second)

elif operator == '-':
    print (first - second)

elif operator == '*':
    print (first * second)

elif operator == '/':
    print (first / second)

elif operator == '%':
    print (first % second)

else :
    print ('Invalid operation')