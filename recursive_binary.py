def binary(arr, first,last,target):
    if first<=last:
        mid = (first+last)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary(arr , mid+1 , last , target)
        else:
            return  binary(arr , first , mid-1 , target)

    else:
        return -1

numbers = [1,2,3,4,5,6,7,8,9]
print(binary(numbers , 0 , len(numbers) , 3))
