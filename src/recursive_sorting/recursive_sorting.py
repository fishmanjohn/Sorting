# TO-DO: complete the helpe function below to merge 2 sorted arrays
array = []

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # pointers say where in the arrays to be removing and adding from and help index the loops 
    i = 0 
    x = 0
    y = 0 
    while i < len(arrA) and x < len(arrB):
        # which is smaller the first index of a or b
        if arrA[i] > arrB[x]:
            #add desired input to merged array and move on
            merged_arr[y] = arrB[x]
            y = y + 1
            x = x + 1
        else:
            #add desired input to merged array and move on
            merged_arr[y] = arrA[i]
            y = y + 1 
            i = i + 1

    while i < len(arrA):
        # handle the rest of the array A
        merged_arr[y] = arrA[i]
        y = y + 1 
        i = i + 1

    while x < len(arrB):
        # handle the rest of the array b
        merged_arr[y] = arrB[x]
        y = y + 1
        x = x + 1

    return merged_arr

print(merge([1,2,3],[4,5,6]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr
    else:
        # break arr into arr1 and arr2
        mid_point = len(arr) // 2 
        arr1 = arr[:mid_point]
        arr2 = arr[mid_point:]
        # chop arr1 and arr2 into little bits AND COLECT THEM!
        narr1 = merge_sort(arr1)
        narr2 = merge_sort(arr2)
    # feed those bits to the merger
        return merge(narr1,narr2)

print(merge_sort(array))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
