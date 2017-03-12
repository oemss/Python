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


def equal(lst1, lst2):
    map(lambda x, y: x >= y, lst1, lst2)


# Функция для получение статистики
# lst - список который надо добавить
# stat - существующая статистика
def add2stat(lst, stat):
    # ind_str = ",".join(map(lambda x: str(x), lst))
    temp_lst = []
    lst = list(map(lambda x: int(x), lst))
    if not stat:
        stat = ([lst, 1])
        return stat
    for el in stat:
        if el[0] == lst:
            temp_lst.append([el[0], el[1]+1])
        else:
            if el[0][0] == lst[0] and el[0][1] > lst[1]:
                temp_lst.append([lst, 1])
                temp_lst.append(stat[stat.index(el):])
            else:
                temp_lst.append(el)
    return temp_lst

        # if temp == -1:
        #     return stat
        #     stat.append(ind_str + ":1")
        # else:                                                                  # Старый кусок говна
        #     stat.append(ind_str + ":" + str(int(el[el.find(":")+1:]) + 1))
        #     stat.pop(temp)
        #     return stat


def combination(lst):
    res = []
    while lst:
        res += [lst]
        lst = lst[1:]
    return res


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
