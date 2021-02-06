# functions are a way to call code whenever you want

def makeList(number): # a function that makes a list of numbers
    if number < 0 or not isinstance(number, int):
        return 'can\'t do that'
    else:
        array = []
        for i in range(number):
            array.append(i)
        return array

# print(makeList(1))
# print(makeList(10))
# print(makeList(100))
# print(makeList(-1))
# print(makeList(.5))

def addition(a,b=1): #function with a default value
    return a+b

# print(addition(3,5))
# print(addition(10))
# print(addition('hello ', 'world'))

def factor(number): # a function that factors numbers
    factors = {}

    counter = 0

    while number % 2 == 0:
        number /= 2
        counter += 1

    if counter > 0:
        factors[2] = counter

    ceil = int(number**(.5)) + 1

    for i in range(3, ceil, 2):
        counter = 0
        while number % i == 0:
            number /= i
            counter += 1
        if counter > 0:
            factors[i] = counter

    if number > 1:
        factors[int(number)] = counter

    return factors

# print(factor(30))
# print(factor(27720))
# print(factor(3992003))
