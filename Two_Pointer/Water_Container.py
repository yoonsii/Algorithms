# Given an unsorted array. 

arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]

p1 = 0

p2 = len(arr) - 1

OldArea = 0

while p1 < p2:
    area = min(arr[p1], arr[p2]) * (p2 - p1)

    if area > OldArea:
        OldArea = area

    if arr[p1] < arr[p2]:
        p1 = p1 + 1
    else:
        p2 = p2 - 1

print(OldArea)