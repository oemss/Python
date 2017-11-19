import pandas as pd
import matplotlib.pyplot as plt
import itertools
import numpy as np


def createplot(lst, ln):
    tdict = {}
    i = 0
    for el in list(itertools.product(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18'], repeat = ln)):
        tdict[i] = lst.get(el, 0)
        i += 1
    print(tdict)
    print(tdict.keys())
    print(tdict.values())
    x = tdict.keys()
    y = tdict.values()
    print(len(x),len(y))
    # plt.bar(tdict.keys(), tdict.values())
    # plt.xticks(tdict.keys())
    plt.plot(x,y)
    plt.show()
    # ts = pd.Series(tdict.values(), index = tdict.keys())
    # ts = ts.cumsum()
    # ts.plot()
