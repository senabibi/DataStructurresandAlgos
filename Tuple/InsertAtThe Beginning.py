
def insert_value_front(input_tuple, value_to_insert):
    new_tuples=(value_to_insert,)+input_tuple
    return new_tuples
    


input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)
