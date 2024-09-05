def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)

print_params(b = 25, c = [1,2,3])

values_list = [44,'five',False]

values_dict = {'a': 21 , 'b': True , 'c': 'berry'}

print_params(*values_list)
print_params(**values_dict)
values_list_2 = [482, 'Python']
print_params(*values_list_2, 42 +3)
