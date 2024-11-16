arrr = [3, 4, 5, 1, 2, 7, 8, 10, 13] # sorted = 1,2,3,4,5,7,8,10,13  target = 10

arrr.sort()

def binarysearch_iterative(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high :
        mid = (low + high) // 2
        print(mid)
        if arr[mid] == target:
            print("found")
            return mid;
        elif arr[mid] > target :
            high = mid - 1
        else:
            low = mid + 1
        print("new mid")
        print(mid)

binarysearch_iterative(arrr, 10)
