def selection_sort(list):
    for j in range(0, len(list)):
        min = j

        for i in range(j + 1, len(list)):
            if list[i] < list[min]:
                min = i

        list[j], list[min] = list[min], list[j]


list = [12, 43, 90, 5, 10]
selection_sort(list)
print(list)
