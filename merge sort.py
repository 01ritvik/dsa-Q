def merge_sort(my_array):
    if len(my_array) == 1:
        return my_array

    middle = len(my_array)//2
    left = my_array[0:middle]
    right = my_array[middle:]

    left_result = merge_sort(left)
    right_result = merge_sort(right)
    return merge(left_result,right_result)

def merge(left_result, right_result):
    result = [None] * ( len(left_result) + len(right_result) )
    i = j = k = 0
    while i<len(left_result) and j < len(right_result):
        if left_result[i] < right_result[j]:
            result[k] = left_result[i]
            i = i+1
        else:
            result[k] = right_result[j]
            j = j+1
        k = k+1

    while i < len(left_result):
        result[k] = left_result[i]
        i = i+1
        k = k+1

    while j < len(right_result):
        result[k] = right_result[j]
        j = j+1
        k = k+1
    return result

numbers = [4,5,6,1,3,7,2]
print(merge_sort(numbers))
