def filter_dict(input_dict, condition):
    return {k: v for k, v in input_dict.items() if condition(k, v)}

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)

print(filtered_dict)
