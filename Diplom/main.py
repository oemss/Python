import time
result = 'result.txt'
swap = 'swap.txt'
input_text = 'input.txt'
import pymorphy2




def buildlist(lst1, lst2):
    if lst2:
        return [lst1 + [lst2[0]]] + buildlist(lst1, lst2[1:])
    else:
        return []


# i - длина последовательности
def create_subseq(i, list, othList):
    templist = []
    if i - 1 == len(list):
        return buildlist(list, othList)
    else:
        if len(othList)+len(list) == i:
            return [list+othList]
        else:
            k = 0
            while len(othList) >= k+i:
                templist = templist + create_subseq(i, list + [othList[k]], othList[k+1:])
                k += 1
            return templist


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
        if split_text[-1]:  # Удаляем лишний элемент если он есть
            split_text.remove([''])
    split_text = list(map(lambda x: x, split_text))
    print("sp= ",split_text)
    return split_text


# Функция для получение статистики
# lst - список который надо добавить
# stat - существующая статистика
def add2stat(lst, stat):
    if stat.get(lst) is None:
        stat[lst] = 1
    else:
        stat[lst] = stat[lst] + 1
    return stat


# Вариант для цепочек длины 2
# Все варианты длины 2, идущие по порядку
def build_combination(lst):
    res = []
    temp = lst
    for i in lst:
        temp = temp[1:]
        if len(temp) != 0:
            for k in temp:
                res.append((int(i), int(k)))
    return res


def get_result():
    res = {}
    for lst in split_txt():
        temp = create_subseq(3,[],lst)
        print(temp)
        for tplst in temp:
            res = add2stat(tuple(tplst), res).copy()
    return res


# print(get_result

