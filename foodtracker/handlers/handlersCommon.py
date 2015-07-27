import collections

def reverseDict(dict):
    result =collections.OrderedDict()
    
    for key in list(reversed(dict.keys())):
        result[key] = dict[key]
        
    return result