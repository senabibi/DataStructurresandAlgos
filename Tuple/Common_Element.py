
def common_elements(tuple1, tuple2):
   tup=()
   for i in tuple1:
       for j in tuple2:
           if i==j:
               tup+=(i,)
   return tup
               





tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  

