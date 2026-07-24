def normalize(lst,start = 0, end = 1):
    lst = (lst - lst.min()) / (lst.max()-lst.min()) * (end - start) + start
    return lst