# print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
# print ('Division without the remainder: ',7 // 3)   # 2
# Complex numbers
# print('Complex number: ', 1 + 1j)
# print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
# print('True == True: ', True == True)
# print('True == False: ', True == False)
# print('False == False:', False == False)


# x1 = float (input('enter x1: '))
# y_0 =  2 * x1 - 2
# y1 = float (input('enter y1: '))
# x_0 = (y1 + 2) / 2



# print(y_0)
# print(x_0)
# intercept = y_0/x_0
# Equation: y = 2x - 2

# x1, y1 = (6, 10)
# x2, y2 = (2, 2)

# m = (y2 - y1)/(x2 - x1)

# print (m)

# x = float(input('输入x 的值： '))
# y = x ** 2 + 6 * x + 9

import math

def func (a, b, c):

    if ( b * b - 4*a*c) < 0:
        print('This eqution no solution')
    elif (b * b - 4*a*c) == 0:
        print('This eqution has one solution')
        return (0-b + math.sqrt(b * b - 4*a*c)/(2 * a ))
    else:
        print ('This eqution has two slution')
        return(0-b + math.sqrt(b * b - 4*a*c)/(2 * a ), 0-b - math.sqrt(b * b - 4*a*c)/(2 * a ))

if __name__ == '__main__':
    a = eval(input("Please enter two item coefficent: "))
    b = eval(input("Please enter one item coefficent: "))
    c = eval(input("Please enter constant coefficent: "))
    list = func(a, b, c)
    print (list)

    

