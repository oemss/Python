result = 'result.txt'
swap = 'swap.txt'
input_text = 'input.txt'

# Поиск элемента в списке
def find_el(sp, sym):
    if not sp:
        return True
    else:
        if sp[0] == sym:
            return False
        else:
            return find_el(sp[1:], sym)


# Список всех предложений заканчивающихся на '.'
def split_txt():
    with open(input_text) as file:
        split_text = list(map(lambda x: x.split(' '), map(lambda x: x.strip(' '), file.read().split('.'))))
        file.close()
        if not find_el(split_text, ['']):  # Удаляем лишний элемент если он есть
            split_text.remove([''])
    return split_text


# Функция для получение статистики
def add2stat(lst, stat):
    ind_str = ",".join(map(lambda x: str(x), lst))
    if not stat:
        stat.append(ind_str + ":1")
        return stat
    for el in stat:
        temp = el.find(ind_str)
        if temp == -1:
            stat.append(ind_str + ":1")
            return stat
        else:
            stat.append(ind_str + ":" + str(int(el[el.find(":")+1:]) + 1))
            stat.pop(temp)
            return stat


def build_collection(lst):

print(split_txt())
