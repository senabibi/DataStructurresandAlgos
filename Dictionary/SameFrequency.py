def check_same_frequency(list1, list2):
    my_dict1={}
    my_dict2={}
    flag=0
    for i in list1:
        value=list1.count(i)
        my_dict1[i]=value
        
        
    for i in list2:
        value=list2.count(i)
        if value==my_dict1[i]:
            flag+=1
        my_dict2[i]=value
     
    if flag==len(my_dict2):
        return True
    else:
        return False
        
