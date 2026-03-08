# ========================================================================================================================
# Python Fundamentals
# ========================================================================================================================

# Função de impressão print

print("Hello Ciro Ávila", 1985, "Oubrubro")

print("Hello Ciro Ávila", 1985, "Oubrubro", sep='$')

print('''Hello Ciro Ávila. This is fulano. How are you? 
How is day.''')

print("Hello 'Ciro Ávila'. This is fulano. How are you?")

print('Hello \'Ciro Ávila\'. This is fulano. How are you?')



# ========================================================================================================================
# Python Variables
# ========================================================================================================================

my_var = 'Ciro'
print(my_var)

x = 10
print(my_var,x)

y = 5
print(x+y)

last_name = 'Ávila'
print(my_var+last_name)

# Dará TypeError: unsupported operand type(s) for +: 'int' and 'str'.
# Os datatypes são diferentes.
# print(x+my_var)

x, y, z = 10, 5, 20
print(x, y, z)

x = y = z = 10
print(x, y, z)

# Comentário de 1 linha, pode ser no título ou na linha de um scrip

''' Comentário de mais de 1 linha pode ser com três aspas simples
ou aspas duplas. '''

# Dará IndentationError: unexpected indent. Precisa colocar \ ao final
# total_sum = 10 + 20
#             + 30 + 20 + 20 + 10
# print())total_sum)

total_sum = 10 + 20 \
            + 30 + 20 + 20 + 10
print(total_sum)

# Também pode-se usar
total_sum = 10 + 20 \
            + 30 + 20 + 20 + 10
print(total_sum)


# Conversão
a = 10
b = '10'
print(type(b))

b_new = int(b)
print(type(b_new))



# ========================================================================================================================
# Python String Formatting
# ========================================================================================================================

''' string funciona como array, ou seja, estrutura de dados que armazena
vários valores do mesmo tipo em posições organizadas e indexadas '''
x = 'Ciro'
print(x[0])


''' Matriz: É uma estrutura bidimensional (2 dimensões), ou seja, array de arrays.
Ex.: [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]'''

x = 'ciroavila'
print(x[0:4])
print(x[4:7])

x = 'Ciro Ávila de Sousa'

print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.replace('s', 'z'))

# o espaço é um delimitador em python

# Uso do split transforma a variável em uma lista.

# Split: Função que transforma uma string em lista baseado em um delimitador.

print(type(x))
my_list = x.split(' ')
print(type(my_list))
print(my_list)

file = 'raw_data.csv'

if (file.endswith('.csv')):
    print('CSV File')

file = 'raw_data.json'
if (file.endswith('.json')):
    print('JSON File')

file = 'raw_data.csv'

if (file.startswith('raw')):
    print('RAW File')

statement = ''' Hello Ciro. What are you doing. Hey Ciro. 
I am talking to you.'''
print(statement.count('Ciro'))

demo_str = 'Hello'
demo_int = 10

print(demo_str.isnumeric())

# print(demo_int.isnumeric())
# AttributeError: 'int' object has no attribute 'isnumeric' porque é função apenas para strin
demo_int = '10'
print(demo_int.isnumeric())

demo_int = '10abc'
print(demo_int.isnumeric())

demo_int = '10abc'
print(demo_int.isalnum())



# ========================================================================================================================
# Conditionals in Python
# ========================================================================================================================

x = 200
if (x==10):
    print('x is 10')
elif (x>100):
    if((x>100) & (x<200)):
        print('Between 100 & 200')
    else:
        print('Greater than 200')
else:
    print('x is not 10')


# ========================================================================================================================
# Loops in Python
# ========================================================================================================================

my_list = ['order', 'products', 'customers']

for i in my_list:
    print(i)

# Sem não ofsse o for, precisaria repetir o print
# print('order')
# print('products')
# print('customers')

for i in range(1,101):
    print(i)

tb_list = ['Order', 'products', 'customers']

for i in tb_list:

    if (i.lower() == 'order'):
        print('Table Order')
    else:
        print('No Table Order')

tb_list = ['Order', 'products', 'customers']

for i in tb_list:
    print(i)
    for x in i:
        print(x)

# continuar 1:35