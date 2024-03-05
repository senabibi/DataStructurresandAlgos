def remove_duplicates(arr):
    r=0
    for i in range(len(arr)):
        if i==len(arr)-r:
                break
        if arr[i]==arr[i+1]:
            arr.remove(arr[i])
            r+=1
            
    return print(arr)
            




remove_duplicates([1, 1, 2, 2, 3, 4, 5])

