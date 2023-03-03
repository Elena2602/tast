#Первая задача:
#Задаем длину списка наполненного рандомными числами от 1 до 100.
#Вводим искомое число X
#Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
#которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

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



#Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
#ценность. В случае с английским алфавитом очки распределяются так:
#● A, E, I, O, U, L, N, S, T, R – 1 очко;
#● D, G – 2 очка;
#● B, C, M, P – 3 очка;
#● F, H, V, W, Y – 4 очка;
#● K – 5 очков;
#● J, X – 8 очков;
#● Q, Z – 10 очков.
#А русские буквы оцениваются так:
#● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#● Д, К, Л, М, П, У – 2 очка;
#● Б, Г, Ё, Ь, Я – 3 очка;
#● Й, Ы – 4 очка;
#● Ж, З, Х, Ц, Ч – 5 очков;
#● Ш, Э, Ю – 8 очков;
#● Ф, Щ, Ъ – 10 очков.
#Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#Будем считать, что на вход подается только одно слово, которое содержит либо только
#английские, либо только русские буквы.
#Ввод:
#ноутбук
#Вывод:#
#12


N = abs(int(input('Введите 1, если играем в английской раскладке, либо 0, если в русской: ')))
eng_dic = {1:'AEIOULNSTR',2:'DG',3:'BCMP',4:'FHVWY',5:'K',8:'JZ',10:'QZ'}
rus_dic = {1:'АВЕИНОРСТ',2:'ДКЛМПУ',3:'БГЁЬЯ',4:'ЙЫ',5:'ЖЗХЦЧ',8:'ШЭЮ',10:'ФЩЪ'}
word = input('Введите слово: ').upper()
if N == 1:
	print('Вы получаете', sum([k for i in word for k, v in eng_dic.items() if i in v]), 'очков')
elif N == 0:
	print('Вы получаете', sum([k for i in word for k, v in rus_dic.items() if i in v]), 'очков')

