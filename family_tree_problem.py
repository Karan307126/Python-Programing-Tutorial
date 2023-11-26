def family_tree(root_gender, n, k):
    noOfChild = pow(2, n - 1)
    if k > noOfChild:
        print("Incorrect Input.")
        return;

    if n == 1:
        return root_gender
    
    if k <= noOfChild / 2:
        return family_tree(root_gender, n - 1, k)
    
    else:
        if root_gender == 'male':
            new_gender = 'female'
        else:
            new_gender = 'male'
        
        return family_tree(new_gender, n - 1, k - (noOfChild / 2))


root_gender = input("Enter root gender : ")
n = int(input("Enter value of n : "))
k = int(input("Enter value of k : "))
ans = family_tree(root_gender, n, k)
print(f"The {n}th generation of {k}th child is {ans}.")