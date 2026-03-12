# ========================================================================================================================
# Data Structures in Python
# ========================================================================================================================

## LIST

my_list = [1,2,'Ciro', 'Avila', ['aa','bb','cc']]

print(my_list[0])
print(my_list[2])
print(my_list[4][1])
print(my_list[4][0])
print(my_list[0:3])

my_list = [1,2,'Ciro', 'Avila', 3]
print(my_list[-3:])

print(len(my_list)) #5
print(len(my_list)-3) #2

print(my_list[len(my_list)-3 : len(my_list)])

print(my_list[-3:])

print(my_list[-10:])


my_list = [1,2,'Ciro', 'Avila', 3, 4, 5, 6]

print(my_list[:])
print(my_list[::2]) # o 2 é opcional. Se em branco, 1 é o valor implícito.


my_list = [1,2,'Ciro', 'Avila', 3, 4, 5, 6]

my_list.append('Hero')
print(my_list)

my_list.insert(1, 'Hero')
print(my_list)

my_list.pop()
print(my_list)

my_list = [1,2,3,4,5,6]

for i in reversed(my_list):
    print(i)

my_list.reverse()
print(my_list)

for i in reversed(my_list):
    print(i)

print(my_list)


my_list = [1,2,3,4,5,6]
print(my_list)
print(my_list[::-1])


my_list = [1,2,3,4,5,6]
print(my_list[-3:])
print(my_list[::2])
print(my_list[::-1])

# List Comprehension
# Forma comum de fazer
my_list = [1,2,3,4,5,6]

new_list = []

for i in my_list:
    new_list.append(i*i)

print(new_list)

# Com List Comprehension
my_list = [1,2,3,4,5,6]

new_list = [i*i for i in my_list]
print(new_list)

new_list = [i*i for i in my_list if (i % 2) == 0]
print(new_list)

new_list = [i*i for i in my_list if (i % 2) == 0 if (i != 6)] 
print(new_list)


## DICTIONARY
my_dict = {'x':1, 'y':2, 'z':3}

print(my_dict)

my_dict['x'] = 10
print(my_dict)

my_dict.pop('z')
print(my_dict)

my_dict = {'x':1, 'y':2, 'z':3}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_dict = {'x':1, 'y':2, 'z':3, 'demo':{'a':1, 'b':2, 'c':3}}
print(my_dict)
print(my_dict['demo'])
print(my_dict['demo']['b'])


## SETS

my_set = {1,2,3,4,5}

print(type(my_set))
print(my_set)

my_set = {1,2,3,4,5,5,5,5,5}
print(my_set)

a = {1,2,3,4,5,5,5,5,5}
b= {10,11,3,2,5}

print(a.union(b))
print(a.intersection(b))

a.remove(2)
print(a)

a.add(20)
print(a)

a = {}
print(type(a))

a = set()
print(type(a))


## TUPLE

my_tup = (1,2,3,4,5)
print(my_tup)

my_tuplist = list(my_tup)
print(my_tuplist)

my_tuplist.append(6)
print(my_tuplist)

my_tup = tuple(my_tuplist)
print(my_tup)