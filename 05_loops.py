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


tb_list = ['products', 'Order', 'customers']

for i in tb_list:
    print(i)
    if (i.lower() == 'order'):
        break


tb_list = ['products', 'Order', 'customers']

for i in tb_list:
    if (i.lower() == 'order'):
        continue
    print(i)


x = 1

while (x<11):
    print(x)
    x = x + 1


x = 1

while (1==1):
    print('hello')
    x = x+1

    if (x>10):
        break