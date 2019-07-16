def merge_sort(nlist):
    print("unsorted list", nlist)
    if len(nlist) > 1:
        mid = len(nlist) // 2
        leftHalf = nlist[:mid]
        rightHalf = nlist[mid:]

        merge_sort(leftHalf)
        merge_sort(rightHalf)

        i = 0
        j = 0
        k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                nlist[k] = leftHalf[i]
                i = i + 1
            else:
                nlist[k] = rightHalf[j]
                j = j + 1
            k = k + 1

        while i < len(leftHalf):
            nlist[k] = leftHalf[i]
            i = i + 1
            k = k + 1

        while j < len(rightHalf):
            nlist[k] = rightHalf[j]
            j = j + 1
            k = k + 1
    print("Sorted list", nlist)


lst1 = []
size = int(input("Enter size of the list: \t"))

for i in range(size):
    elements = int(input("Enter an element: \t"))
    lst1.append(elements)

merge_sort(lst1)