def heapsort(list1):
    max_heap(list1)
    for i in range(len(list1) - 1, 0, -1):
        list1[0], list1[i] = list1[i], list1[0]
        max_heap2(list1, index=0, size=i)


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heap(list1):
    length = len(list1)
    start = parent(length - 1)
    while start >= 0:
        max_heap2(list1, index=start, size=length)
        start = start - 1


def max_heap2(list1, index, size):
    l = left(index)
    r = right(index)
    if (l < size and list1[l] > list1[index]):
        largest = l
    else:
        largest = index
    if (r < size and list1[r] > list1[largest]):
        largest = r
    if (largest != index):
        list1[largest], list1[index] = list1[index], list1[largest]
        max_heap2(list1, largest, size)


list1 = input('Enter the list of numbers: ').split()
list1 = [int(x) for x in list1]
heapsort(list1)
print('Sorted list: ', end='')
print(list1)