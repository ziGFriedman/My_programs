# удаление ложных значений (False, None, 0 и «») из списка с помощью filter():
def compact(lst):
    return list(filter(bool, lst))

compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
