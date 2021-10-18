def insertin_sort(list):
    for i in range(1 ,len(list)):
        key = list[i]
        last = i-1

        while last >= 0 and key < list[last]:
            list[last+1] = list[last]
            last = last-1

        list[last+1] = key

list = [12,45,90,3,10]
insertin_sort(list)
print(list)