
def merge_dicts(dict1, dict2):
    
    new={}
    for key,value in dict1.items():
        if key in new:
            new[key]+=value
        else:
            new[key]=value
    
    for key,value in dict2.items():
        if key in new:
            new[key]+=value
        else:
            new[key]=value
    return new
        
        


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))
