import buildpos
import plot

result = 'result.txt'
swap = 'swap.txt'
input_text = 'out.txt'


def eqlst(lst1, lst2):
    if lst1 == lst2:
        return 1
    k = 0
    while k < len(lst1):
        if lst1[k] < lst2[k]:
            return 0
        k += 1
    return 2


def sortlist(list):
    temp1 = []
    i = 0
    while i < len(list):
        temp2 = []
        k = 0
        while k < len(temp1):
            tm = eqlst(temp1[k], list[i])
            if tm == 1:
                break
            else:
                if tm == 2:
                    temp2 += [list[i]] + temp1[k:]
                    temp1 = temp2
                    break
                else:
                    temp2 += [temp1[k]]
                    k += 1
        else:
            temp1 = temp2 + [list[i]]
        i += 1
    return temp1

print("XUYYYY = ",sortlist([[10, 1, 14], [1, 14, 1], [14, 1, 5]]))
def blistinarow(i, step, list):
    res = []
    j = 0
    while j <= len(list):
        k = j
        temp = []
        while k <= len(list):
            if len(temp) == i:
                res += [temp]
                break
            else:
                if k == len(list):
                    break
                temp += [list[k]]
                k += 1
        j += step
    return res


def buildlist(lst1, lst2):
    if lst2:
        return [lst1 + [lst2[0]]] + buildlist(lst1, lst2[1:])
    else:
        return []


# i - длина последовательности
def create_subseq(i, list, othList):
    print(othList)
    templist = []
    if i - 1 == len(list):
        return buildlist(list, othList)
    else:
        if len(othList) + len(list) == i:
            return [list + othList]
        else:
            k = 0
            while len(othList) >= k + i:
                templist = templist + create_subseq(i, list + [othList[k]], othList[k + 1:])
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


def get_result():
    res = {}
    for lst in split_txt():
        lst = list(map(lambda x: int(x),lst))
        # temp = create_subseq(3, [], lst)
        temp = blistinarow(3, 1, lst)
        print("1 = ",temp)
        temp = sortlist(temp)
        print("2 = ", temp)
        for tplst in temp:
            res = add2stat(tuple(tplst), res).copy()
    return res



buildpos.createposfile()
ress = get_result()
print("12312", ress)
# plot.plotbar(ress.values(), ress.keys())
