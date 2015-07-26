import collections
def xstr(s):
    return 0 if s is None else s
    
def getTotalFatCount(i):
    return round(xstr(i['FA_Sat']) + xstr(i['FA_Mono']) + xstr(i['FA_Poly']),2)
    
def reverseDict(dict):
    result =collections.OrderedDict()
    
    for key in list(reversed(dict.keys())):
        result[key] = dict[key]
        
    return result