# sometimes is usefull to run code multiple times, so we use loops for that

array = []

for i in range(100):  # loops 100 times
    if i % 3 == 0:                   # will run code only when the condition is met
        array.append(i)
    elif i % 3 == 1:                 # will run if everything before fails and the condition is met
        array.append('derronie')
    else:
        array.append('is a hoe')     # will run when everything else fails


print(array)

print(len(array))

name_list = ['derronie', 'is', 'learning', 'to', 'code']

for name in name_list:   # you can also loop on arrays
    print(name)

j = 0
array1 = []

while (j < 100):         # you can also loop while a condition is met
    array1.append(j)
    j += 1 #j = j + 1

print(array1)
