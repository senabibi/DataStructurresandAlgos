def middle(lst):
    ll=[]
    l=len(lst)
    split=l//2
    if  l%2==0:
        
        ll.append(lst[split-1])
        ll.append(lst[split])
    else:
        ll.append(lst[split])
    return ll
my_list=[1,2,3,4]
print(middle(my_list))
        
        
