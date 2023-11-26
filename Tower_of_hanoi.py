def towerOfHanoi(n, source, helper, destination):
    if n == 1:
        print(f"Transfer disk {n} {source} to {destination}.")
        return;
    
    towerOfHanoi(n - 1, source, destination, helper)
    print(f"Transfer disk {n} {source} to {destination}.")
    towerOfHanoi(n - 1, helper, source, destination)


n = int(input("Enter number of disk : "))
towerOfHanoi(n, "s", "h", "d")