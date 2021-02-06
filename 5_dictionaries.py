# dictionaries are a usefull data structure

# database aproach

car1 = {'color': 'blue', 'brand': 'tesla', 'model': 'x'}
car2 = {'color': 'red', 'brand': 'tesla', 'model': '3'}
car3 = {'color': 'black', 'brand': 'tesla', 'model': 's'}

cars = [car1, car2, car3]

# for car in cars[::-1]:
#     print(car['brand'] + ' model ' + car['model'] + ' ' + car['color'])

# extract data aproach

number = 27720

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

# print(factors)
# print(factors.keys())   # we can get info on the keys of the dictionary
# print(factors.values()) # we can get info on the
