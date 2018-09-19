from random import randint
l = [randint(-10, 10) for i in range(10)]
square = [number*number for number in l]

print('thats all squares: ', square)
