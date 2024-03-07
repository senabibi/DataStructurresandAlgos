def find(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]==num[j]:
                continue
            elif num[i]+num[j]==target:
                print(num[i],num[j])


print(find([1,2,3,4,5,6],6))

##Leetcode Answer
def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i

