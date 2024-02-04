
def reverse_dict(my_dict):
    new={}
    for key,value in my_dict.items():
        new_value=key
        new_key=value
        new[new_key]=new_value
    return new
        




my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))
