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