def sort(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp


n = int(input("Enter the number : "))

list = []

for i in range(n):
    ele = int(input("Enter the list elements : "))
    list.append(ele)
print(f"Before sorting {list}.")
sort(list)
print(f"After sorting {list}.")