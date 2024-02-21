with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        recipie_name = line.strip()
        ingredients_count = f.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recipie = f.readline().strip().split(' | ')
            product, quantity, word = recipie
            ingredients.append({'ingredient_name': product, 'quantity': int(quantity), 'measure': word})
        f.readline()
        cook_book[recipie_name] = ingredients
print(cook_book)


def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for compound in cook_book[dish]:
                if compound['ingredient_name'] in result:
                    result[compound['ingredient_name']]['quantity'] += compound['quantity'] * person_count
                else:
                    result[compound['ingredient_name']] = {'measure': compound['measure'],'quantity': (compound['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)
get_shop_list_by_dishes(10, ['Запеченный картофель', 'Омлет'])
