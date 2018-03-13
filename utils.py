def userDictToString(list):
    ret = []
    for x in list:
        ret.append(x['pseudo'] + ' - ' + x['class'] + ' - ' + x['ilvl'])
    if len(ret) < 3 :
        for i in range (0, 3-len(ret)):
            ret.append('')
    return ret

def userStringToString(list):
    res = ''
    for i in list:
        if i != '':
            res += '[' + i + '] > '
    return res

def dictListToList(list):
    res = []
    for i in list:
        res.append(i.values())
    return res


