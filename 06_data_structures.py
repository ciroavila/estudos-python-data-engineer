# ========================================================================================================================
# Data Structures in Python
# ========================================================================================================================

# List

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

# https://www.youtube.com/watch?v=ZvU7lupoXQE
# 2:00:21
