# Description: Given an array of integers nums, find all unique triplets (a, b, c) in the array such that:

#     a+b+c=0
#     a,b,c are distinct numbers (i.e., no duplicates).


AnswerSet = []

nums = [-1, 0, 1, 2, -1, -4]
#nums = [-1, 1, 0, 2, -2, -1]
#nums = [-10, -7, -3, -2, 0, 1, 3, 5, 6, 9]


nums.sort()

p1 = 1
p2 = len(nums) - 1

# Take 4

for i in range(len(nums)):

    if i < 0 and nums[i] == nums[i - 1]:
        continue

    p1 = i + 1
    p2 = len(nums) - 1    

    target = nums[i]


    while p1 < p2: 
        currSum = nums[p1] + nums[p2]

        if currSum == -target:
            #print(nums[p1],nums[p2],target)
            AnswerSet.append((target, nums[p1], nums[p2]))
            
            while p1 < p2 and nums[p1] == nums[p1 + 1]:
                p1 += 1
            while p1 < p2 and nums[p2] == nums[p2 - 1]:
                p2 -= 1

            # Move pointers after skipping duplicates
            p1 += 1
            p2 -= 1
        elif currSum < -target:
            p1 += 1
        elif currSum > -target:
            p2 -= 1

        
print(AnswerSet)

# Things I had to work on:

# Summary of Fixes (First Draft to Final Solution):

# 1. **Resetting Pointers:**
#    - Fixed incorrect pointer reset logic. Now, `p1 = i + 1` and `p2 = len(nums) - 1` at the start of each iteration of the outer loop.

# 2. **Duplicate Target Handling:**
#    - Added logic to skip duplicate targets in the outer loop:
#      ```python
#      if i > 0 and nums[i] == nums[i - 1]:
#          continue
#      ```

# 3. **Duplicate Skipping for Pointers:**
#    - After finding a valid triplet, skip duplicate values for `p1` and `p2`:
#      ```python
#      while p1 < p2 and nums[p1] == nums[p1 + 1]:
#          p1 += 1
#      while p1 < p2 and nums[p2] == nums[p2 - 1]:
#          p2 -= 1
#      ```

# 4. **Avoid Unnecessary Resets:**
#    - Removed redundant resets of `p1` and `p2` after processing a target.

# 5. **Improved Deduplication Logic:**
#    - Deduplicated triplets during the main loop rather than relying on post-processing.




# Take 1

# for target in nums:

#     while p1 < p2:
#         currSum = nums[p1] + nums[p2]
#         print(currSum)
#         if currSum == -target:
#             print(nums[p1],nums[p2],target)
#             p1 = 0
#             p2 = len(nums) - 1
#             break
#         elif currSum < -target:
#             p1 += 1
#         elif currSum > -target:
#             p2 -= 1
#     else:
#         print("not found for", target)
#         p1 = 0
#         p2 = len(nums) - 1
    

# Take 2

# for index, target in enumerate(nums):
#     print(index)

#     while p1 < p2:
#         currSum = nums[p1] + nums[p2]
#         # print(currSum)
#         if currSum == -target:
#             print(nums[p1],nums[p2],target)
#             p1 = 0
#             p2 = len(nums) - 1
#             break
#         elif currSum < -target:
#             if (nums[p1 + 1]) == target:
#                 break
#             else:
#                 p1 += 1
#         elif currSum > -target:
#             if (nums[p2 - 1]) == target:
#                 break
#             else:           
#                 p2 -= 1
#     else:
#         print("not found for", target)
#         p1 = 0
#         p2 = len(nums) - 1
    


# Take 3

# for target in nums:

#     while p1 < p2:

#         currSum = nums[p1] + nums[p2]

#         #print(currSum)

#         if currSum == -target:
#             #print(nums[p1],nums[p2],target)
#             AnswerSet.append((nums[p1],nums[p2],target))
#             p1 = 0
#             p2 = len(nums) - 1
#             break
#         elif currSum < -target:
#             p1 += 1
#         elif currSum > -target:
#             p2 -= 1
#     else:
#         #print("not found for", target)
#         p1 = 0
#         p2 = len(nums) - 1
    


# #triplets = [(1, 2, 3), (1, 0, 3), (3, 0, 1)]

# # Use a set to store unique triplets
# unique_triplets = set()

# # Normalize each triplet by sorting its elements
# for triplet in AnswerSet:
#     sorted_triplet = tuple(sorted(triplet))  # Sort and convert back to tuple
#     unique_triplets.add(sorted_triplet)     # Add to set

# # Convert back to a list (if needed) and print
# unique_triplets = list(unique_triplets)
# print(unique_triplets)
