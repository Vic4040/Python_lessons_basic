from random import randint
l = [randint(-10, 10) for i in range(10)]


numbers = [x for x in l if x % 3 == 0 and x > 0 and x % 4 != 0]

print('числа кратные 3 и не кратные 4: ', numbers)