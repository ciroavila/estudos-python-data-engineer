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