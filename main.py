import random
my_list = int(input('Введите искомое число X: '))
my_dict = []
new_list = 0
new = -1

for i in range(20):
     my_dict.append(random.randint(1,101))
     min_d = max(my_dict) - my_list

     if int(my_dict[i]) == my_list:
         new_list += 1

for i in set(my_dict):
     if abs(i - my_list) < min_d:
         min_d = abs(i - my_list)
         new = i
print(f'Встречется {new_list} раз ')


print(f'Максимально близкое число: {new}')

print(f'Список: {my_dict}')
