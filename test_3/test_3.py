import wikipediaapi

wiki = wikipediaapi.Wikipedia('ru')

page = wiki.page('Категория:Животные по алфавиту')


def get_animals_count(page, template):
    animals = [cat.title for cat in page.categorymembers.values()]
    for animal in animals:
        letter = animal[0]
        if letter in template.keys():
            template[letter] = template[letter] + 1
    return template


output = {
    'А': 0, 'Б': 0, 'В': 0, 'Г': 0, 'Д': 0, 'Е': 0, 'Ё': 0, 'Ж': 0, 'З': 0, 'И': 0,
    'Й': 0, 'К': 0, 'Л': 0, 'М': 0, 'Н': 0, 'О': 0, 'П': 0, 'Р': 0, 'С': 0, 'Т': 0,
    'У': 0, 'Ф': 0, 'Х': 0, 'Ц': 0, 'Ч': 0, 'Ш': 0, 'Щ': 0, 'Э': 0, 'Ю': 0, 'Я': 0,
}

   
if __name__ == '__main__':
    animals_count = get_animals_count(page, output)
    for letter, count in animals_count.items():
        print('{letter} : {count}'.format(letter=letter, count=count))
