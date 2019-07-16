list1 = []
num = int(input('how many numbers to enter:'))
print('enter values:')
for k in range(num):
    list1.append(int(input()))

print('unsorted list:',list1)

for j in range(len(list1)-1,0,-1):
    for i in range(j):
        if list1[i] > list1[i+1]:
            list1[i],list[i+1] = list[i+1],list[i]
            print(list1)
        else:
            print(list1)
        print()

print("sorted list:", list1)