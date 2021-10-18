def linear(array , target):
    for i in range(0,len(array)):
        if array[i] == target:
            print("target found at: " , i)

linear([1,2,3,4,5,6] , 4)