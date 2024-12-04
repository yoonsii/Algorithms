# Description: Given an array of integers nums, find all unique triplets (a, b, c) in the array such that:

#     a+b+c=0

#     a,b,c are distinct numbers (i.e., no duplicates).

nums = [-1, 0, 1, 2, -1, -4]

nums.sort()

p1 = 0
p2 = len(nums) - 1

# [-4, -1, -1, 0, 1, 2]



for target in nums:

    while p1 < p2:
        currSum = nums[p1] + nums[p2]
        print(currSum)
        if currSum == -target:
            print(nums[p1],nums[p2],target)
            p1 = 0
            p2 = len(nums) - 1
            break
        elif currSum < -target:
            p1 += 1
        elif currSum > -target:
            p2 -= 1
    else:
        print("not found for", target)
        p1 = 0
        p2 = len(nums) - 1
    


    






