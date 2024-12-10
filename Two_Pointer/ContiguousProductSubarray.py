# Problem: Subarray Product Less Than K

# Description:
# Given an array of positive integers nums and an integer k, find the number of contiguous subarrays where the product of all elements is less than k.

# Hint we don't need to actually output the arrays. We just need to provide the count.
# 

nums = [10, 5, 2, 6]
k = 100

p1 = 0
p2 = 0

currentProduct = 1

resultCount = 0

for i in range(p1,p2+1):
    print(i)


while p2 <= len(nums) - 1:
    result = 1
    for i in range(p1,p2+1):
        result = result * nums[i]
        
    if result < k :
        resultCount += (p2 - p1 + 1)

        if p2 <= len(nums) - 1:
            p2 += 1
        

    elif result >= k:
        if p1 <= len(nums) - 1:
            p1 += 1  
        

    print(resultCount)



    