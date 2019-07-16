def quicksort(list1, start, end):

    if end - start > 1:
        p = portion(list1, start, end)
        quicksort(list1, start, p)
        quicksort(list1, p + 1, end)


def portion(list1, start, end):
    p1 = list1[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and list1[i] <= p1):
            i = i + 1
        while (i <= j and list1[j] >= p1):
            j = j - 1

        if i <= j:
            list1[i], list1[j] = list1[j], list1[i]
        else:
            list1[start], list1[j] = list1[j], list1[start]
            return j


list1 = input('Enter the list of numbers: ').split()
list1 = [int(x) for x in list1]
quicksort(list1, 0, len(list1))
print('Sorted list: ', end='')
print(list1)