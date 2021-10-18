def binary_search(array , target):
    first = 0
    last = len(array) - 1

    while first <= last:
        midpoint = (first+last)//2

        if array[midpoint] == target:
            return midpoint
        elif array[midpoint] > target:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return  -1

print(binary_search([1,2,3,4,5,6,7,8] , 6))

