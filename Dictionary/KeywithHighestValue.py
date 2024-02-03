
def max_value_key(my_dict):
    max_key=max(my_dict,key=my_dict.get)
    return max_key
    


my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))
