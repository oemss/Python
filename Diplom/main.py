def find_el(sp, sym):  # Поиск элемента в списке
    if not sp:
        return True
    else:
        if sp[0] == sym:
            return False
        else:
            return find_el(sp[1:], sym)


with open('text.txt') as file:
    split_text = list(map(lambda x: x.split(' '), map(lambda x: x.strip(' '), file.read().split('.'))))  # Список всех
    # предложений заканчивающихся на '.'
    file.close()
    if not find_el(split_text, ['']):  # Удаляем лишний элемент если он есть
        split_text.remove([''])


def add2stat(fst, snd):
    op


def allcombination(st_list):
    map(lambda x: )