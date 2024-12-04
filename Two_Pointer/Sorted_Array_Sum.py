arr = [1,3,4,9,12,16,20]

for i in arr:
    print(i)


target = 17
min = 0
max = len(arr) -1
currSum = 0
count = 0

# for x in range(len(arr)):
#     print("min",min)
#     print("max",max)

#     currSum = arr[min] + arr[max]

#     if (count > ((len(arr) // 2 ) + 1) ):
#         print("not found)")
#         break
#     elif (currSum == target):
#         print(min, ",", max)
#         break

#     elif (currSum > target):
#         max = max - 1
#     elif (currSum < target):
#         min = min + 1
    
#     count = count+1
    

# Improved version - after critique

min = 0
max = len(arr) - 1

while (min < max):
    currSum = arr[min] + arr[max]
    if (arr[min] + arr[max] == target):
        print(min, ",", max)
        break
    elif (currSum > target):
        max = max - 1
    elif (currSum < target):
        min = min + 1

# Final version - Handles edge cases

min = 0
max = len(arr) - 1

while min < max:
    currSum = arr[min] + arr[max]
    if currSum == target:
        print("Found indices:", min, ",", max)
        break
    elif currSum > target:
        max -= 1
    else:  # currSum < target
        min += 1
else:
    print("No solution found.")
