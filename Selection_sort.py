def sort(list):
    for i in range(len(list) - 1):
        min = i
        for j in range(i , len(list)):
            if list[j] < list[min]:
                min = j
        
        temp = list[i]
        list[i] = list[min]
        list[min] = temp
        print(list)




n = int(input("Enter the number : "))

list = []

for i in range(n):
    ele = int(input("Enter the list elements : "))
    list.append(ele)
print(f"Before sorting {list}.")
sort(list)
print(f"After sorting {list}.")