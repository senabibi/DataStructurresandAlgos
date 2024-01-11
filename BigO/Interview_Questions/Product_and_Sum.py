def foo(array):
    sum=0
    product=1
    for i in array:
        sum+=i
    
    for i in array:
        product*=i
    print(f"Sum ={sum}, Product={product}")
