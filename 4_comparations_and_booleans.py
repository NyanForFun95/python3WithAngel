# comparisons always return a boolean

# == is equal as comparer, works with strings and booleans

print(1==1)
print(1=='1')
print(1==2)
print('hola'=='hello')
print(True==True)

# < and > work as expected

print(1<2)
print(1>2)
print(1<1)

# <= and >= allow the equality

print(1<=1)

# != means different, works with stings and booleans

print(1!=1)
print(1!=2)
print(True!=True)

# booleans have operations too!

# not is negation

print(not True)

# and gives true if both are true and false otherwise

print(True and False)
print(False and False)
print(True and True)

# or gives true if either is true, and false otherwise

print(True or False)
print(False or False)
print(True or True)

# examples (project euler #1 solution)

counter = 0

for i in range(1000):
    if(i % 3 == 0 or i % 5 == 0):
        counter += i

print(counter)
