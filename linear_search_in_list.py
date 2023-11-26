index = -1

def search(list, x):
    for i in range(0, len(list)):
        globals()["index"] = i
        if list[i] == x:
            return True
    return False


n = int(input("Enter the number : "))

list = []

for i in range(n):
    ele = int(input("Enter the list elements : "))
    list.append(ele)

x = int(input("Enter element you have search : "))

if search(list, x):
    print(f"Found at index {index + 1}.")
else:
    print("Not Found.")