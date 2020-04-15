# TO-DO: Complete the selection_sort() function below 
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for x in range(smallest_index, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x
             



        # TO-DO: swap
        if cur_index != smallest_index:
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr

#print(selection_sort(arr1))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(1, len(arr)):
        for x in range(0, len(arr) - 1):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x+1], arr[x]
    return arr

#print(bubble_sort(arr1))
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

    #This is a change to implement on branch 
    