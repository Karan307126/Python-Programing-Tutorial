class Employee:
    company="Google"
    salary=100

karan=Employee()
tushar=Employee()
print(karan.company)
print(tushar.company)
# Creating instance attribute salary for both the objects
karan.salary=500
tushar.salary=600

Employee.company="YouTube"
print(karan.company)
print(tushar.company)
print(karan.salary)
print(tushar.salary)

# Below line throws an error as address is not present in instance/class 
# print(tushar.address)