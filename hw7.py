import os
from pprint import pprint

#Задача №1

cook_book = {}

with open('recipes.txt', encoding='utf-8') as file:
  for line in file:
    dish_name = line.strip()
    ingredient_count = file.readline()
    ingredient_list = []
    for i in range(int(ingredient_count)):
      ingredient = file.readline()
      ingredient_name, quantity, measure = ingredient.strip().split(' | ')
      ingredient_list.append({
        'ingredient_name': ingredient_name,
        'quantity': int(quantity),
        'measure': measure
      })
      dict_ = {dish_name: ingredient_list}
    empty_line = file.readline()
    cook_book.update(dict_)
print('Задача №1\n')
print('cook_book =')

pprint(cook_book, indent=2, width=150, sort_dicts=False)

#Задача №2

def get_shop_list_by_dishes(dishes,person_count):
  shop_list = {}
  for dish in dishes:
    if dish in cook_book.keys():
      for recipe in cook_book[dish]:
        if recipe['ingredient_name'] in shop_list:
          shop_list[recipe['ingredient_name']]['quantity'] += recipe['quantity'] * person_count
        else:
          shop_list[recipe['ingredient_name']] = {'measure': recipe['measure'], 'quantity': (recipe['quantity'] * person_count)}
    else:
      error = 'Выбранного вами блюда нет в кулинарной книге.'
      return error
  return shop_list
print('\nЗадача №2\n')

pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5), indent=2, width=150, sort_dicts=False)

#Задача №3

text_result = []
for file_line in ['1.txt', '2.txt', '3.txt']:
  with open(os.path.join(file_line), 'rt', encoding='utf-8') as file:
    data = file.readlines()
    text_result .append([file_line + '\n', str(len(data)) + '\n', data])

text_result .sort(key=lambda i: i[1])

with open(os.path.join('text_result.txt'), 'wt', encoding='utf-8') as file:
  for file_line in text_result:
    file.writelines([file_line[0], file_line[1]])
    file.writelines(file_line[2])
    file.write('\n')
