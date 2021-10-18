def bubble_sort(list):
    for j in range(0, len(list)):
        for i in range(0 , len(list) -1 - j):
            if list[i] > list[i+1]:
                list[i] , list[i+1] = list[i+1] , list[i]

list = [12,54,7,90,23]
bubble_sort(list)
print(list)
