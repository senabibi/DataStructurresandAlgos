
def sum_product(input_tuple):
    
    sum_result=0 
    product_result=1 
    for i in input_tuple:
        sum_result+=i 
        product_result*=i 
    return sum_result,product_result
    



input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result) 
