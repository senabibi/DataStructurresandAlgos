
def remove_duplicates(arr):

    if len(set(arr)) < len(arr):
        return True
    

nums = [1,2,3,1]
print(remove_duplicates(nums))
