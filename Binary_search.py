index = -1

def search(list, x):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = ((u + l) // 2)
        if list[mid] == x:
            globals()["index"] = mid
            return True
        else:
            if list[mid] < x:
                l = mid + 1
            else:
                u = mid - 1
    return False



n = int(input("Enter the number : "))

list = []

for i in range(n):
    ele = int(input("Enter the list elements : "))
    list.append(ele)
print(list)
x = int(input("Enter element you have search : "))

if search(list, x):
    print(f"Found at index {index + 1}.")
else:
    print("Not Found.")