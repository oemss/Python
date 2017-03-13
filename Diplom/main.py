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
        if not split_text[-1]:  # Удаляем лишний элемент если он есть
            split_text.remove([''])
    return split_text


# Сравнение двух списков возвращает True, если 2ой "больше" первого
def equal(lst1, lst2):
    print("lst1 = ", lst1)
    print("lst2 = ", lst2)
    if lst1 == []:
        return False
    else:
        if lst1[0] < lst2[0]:
            return True
        else:
            return equal(lst1[1:], lst2[1:])


# Функция для получение статистики
# lst - список который надо добавить
# stat - существующая статистика
def add2stat(lst, stat):
    temp_lst = []
    print(stat)
    lst = list(map(lambda x: int(x), lst))
    if not stat:
        stat = ([[lst, 1]])
        return stat
    for el in stat:
        print("el = ", el)
        if el[0] == lst:
            temp_lst.append([el[0], el[1]+1])
        else:
            if equal(el[0], lst):
                temp_lst.append([lst, 1])
                temp_lst.append(stat[stat.index(el):])
            else:
                temp_lst.append(el)
    return temp_lst


# Вариант для цепочек длины 2
# Все варианты длины 2, идущие по порядку
def build_combination(lst):
    res = []
    temp = lst
    for i in lst:
        temp = temp[1:]
        if len(temp) != 0:
            for k in temp:
                res.append([i, k])
    return res


def get_result():
    res = []
    for lst in split_txt():
        temp = build_combination(lst)
        for tplst in temp:
            res = add2stat(tplst, res)
    return res

# def build_collection(lst):

print(get_result())
