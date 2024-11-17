

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

#binarysearch_iterative(arrr, 10)


def binarysearch_recursive(arr, target):

        mid = (len(arr)) // 2
        print("miid", mid)
        print("target", target)

        print("len ", len(arr))
        if len(arr) == 1:
            if arr[0] == target:
                print("found")
                return
            else:
                print("not found")
                return
        elif arr[mid] == target:
            print("found");
            return
        elif arr[mid] > target:
            binarysearch_recursive(arr[0:mid-1], target)
        else:
            binarysearch_recursive(arr[mid+1:len(arr)], target)
            

#binarysearch_recursive(arrr, 14)


def binarysearch_recursive_improved(arr, target):
    if not arr:  # Base case: empty array
        print("not found")
        return False

    mid = len(arr) // 2
    print("mid", mid)
    print("target", target)
    print("len ", len(arr))

    if arr[mid] == target:
        print("found")
        return True
    elif arr[mid] > target:
        return binarysearch_recursive_improved(arr[:mid], target)  # Left subarray
    else:
        return binarysearch_recursive_improved(arr[mid+1:], target)  # Right subarray

# Example array
arrr = [2, 4, 6, 8, 10, 12, 14, 16, 18]
#print("A")
print(binarysearch_recursive_improved(arrr, 14))  # Output: True
#print("B")
print(binarysearch_recursive_improved(arrr, 7))   # Output: False

""" Key Issues and Fixes:

    Array Slicing Error:
        When searching the left subarray, your slicing arr[0:mid-1] skips the middle element itself. In Python, slicing is exclusive of the end index, so it should be arr[0:mid] instead.

    Base Case with Single Element:
        If the target is not in the array and the length becomes 1, the code will always print "not found" without handling the overall return value properly.
        Instead, explicitly return False or True when the search is complete.

    Redundant len(arr) in Slice:
        You can simplify the slicing for the right subarray. Instead of arr[mid+1:len(arr)], just use arr[mid+1:].

    Return Values Missing:
        Your function doesn't return a value explicitly for all cases. If you want it to propagate results back up the recursion stack, you need to return the result of the recursive calls.

    Efficiency:
        Slicing creates a new list at each recursive call, which is not ideal for performance. Instead, you can pass indices (low and high) to avoid creating new lists.
 """


def binarysearch_recursive_optimized(arr, target, low, high):
    if low > high:  # Base case: search space exhausted
        print("not found")
        return False

    mid = (low + high) // 2
    print("mid", mid)
    print("target", target)
    print("current element", arr[mid])

    if arr[mid] == target:
        print("found")
        return True
    elif arr[mid] > target:
        return binarysearch_recursive(arr, target, low, mid - 1)  # Left subarray
    else:
        return binarysearch_recursive(arr, target, mid + 1, high)  # Right subarray

# Example usage
arrr = [2, 4, 6, 8, 10, 12, 14, 16, 18]
#print(binarysearch_recursive_optimized(arrr, 14, 0, len(arrr) - 1))  # Output: True
#print(binarysearch_recursive_optimized(arrr, 7, 0, len(arrr) - 1))   # Output: False


# Why the Optimized Version is Better:

#     Avoids Array Slicing: Does not create new subarrays, saving memory and improving performance.
#     More General: Can handle arrays of any type without worrying about the cost of slicing.
#     Cleaner Base Case: It explicitly checks for the range of indices rather than relying on array length.