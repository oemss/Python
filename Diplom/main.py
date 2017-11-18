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

# def create_seq(i, seq):
#
#

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


# # Сравнение двух списков возвращает True, если 2ой "больше" первого
# def equal(lst1, lst2):
#     if not lst1:
#         return False
#     else:
#         if lst1[0] < lst2[0]:
#                 if lst1[1] < lst2[1]:
#                     return True
#                 else:
#                     return False
#         else:
#             return equal(lst1[1:], lst2[1:])


# def equal(lst1, lst2):
#     if lst1[0] < lst2[0]:
#         if lst1[1] < lst2[1]:
#             return True
#     return False


# Функция для получение статистики
# lst - список который надо добавить
# stat - существующая статистика
def add2stat(lst, stat):
    # temp_lst = []
    # # lst = list(map(lambda x: int(x), lst))
    # if not stat:
    #     temp_lst.append([lst, 1])
    #     return temp_lst
    # for el in stat:
    #     print("-------------------------")
    #     print("stat = ", stat)
    #     print("temp = ", temp_lst)
    #     print("lst = ", lst)
    #     print("el0 = ", el[0])
    #     if el[0] == lst:
    #         print("1 add = ", [el[0], el[1]+1])
    #         temp_lst.append([el[0], el[1]+1])
    #     else:
    #         # if equal(el[0], lst):
    #         #     print("2 add = ", [lst, 1], el)
    #         #     temp_lst.append([lst, 1])
    #         #     temp_lst.append(el)
    #         # else:
    #         print("3 add = ", el)
    #         temp_lst.append(el)
    # return temp_lst
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


# def build_collection(lst):

# print(get_result
morph = pymorphy2.MorphAnalyzer()
print(morph.parse('стали'))