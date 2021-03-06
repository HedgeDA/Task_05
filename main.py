import pprint


def read_file(filename, book = None):
    if book is None:
        book = dict()

    with open(filename, encoding='utf8') as file:
        recipe_name = ''
        ingridients_count = 0
        ingridients = list()

        for line in file:
            # убираем пустые и служебные символы в конце строки
            rline = line.rstrip()

            if not rline:
                recipe_name = ''
                ingridients_count = 0
                ingridients = list()
                continue

            if not recipe_name:
                recipe_name = rline
            elif ingridients_count == 0:
                try:
                    ingridients_count = int(rline)
                except TypeError:
                    ingridients_count = -1
            else:
                sub_lines = rline.split(" | ")
                if len(sub_lines) == 3:
                    try:
                        ingridient = {'ingridient_name': sub_lines[0],
                                      'quantity': int(sub_lines[1]),
                                      'measure': sub_lines[2]}
                        ingridients.append(ingridient)

                        if len(ingridients) == ingridients_count:
                            book[recipe_name] = ingridients
                    except TypeError:
                        print('Ошибка чтения ингридиента в рецепте блюда:', recipe_name)

    return book


def get_shop_list_by_dishes(dishes, person_count, book):
    ingridients = dict()

    for dish in dishes:
        if book.get(dish) is None:
            print('Блюдо "{}" в книге не найдено!'.format(dish))
            continue

        for ingridient in book[dish]:
            if ingridients.get(ingridient['ingridient_name']) is None:
                ingridients[ingridient['ingridient_name']] = {'measure': ingridient['measure'], 'quantity' : 0}

            ingridients[ingridient['ingridient_name']]['quantity'] += ingridient['quantity'] * person_count

    return ingridients

def main():
    book = read_file('book.txt')

    result = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2, book)
    pprint.pprint(result)


main()
