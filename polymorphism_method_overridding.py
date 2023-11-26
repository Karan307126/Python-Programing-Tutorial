class Father:
    def mobile(self):
        print("Samsung Galexy J2.")
    def laptop(self):
        print("Lenovo.")

class Me(Father):
    def mobile(self):
        print("Redme Note 9.")
    # def laptop(self):
    #     print("Dell Vestro.")

a = Me()
a.laptop()

# if i have no laptop method then my father laptop is my laptop but i have my own laptop them code tell my laptop.
# Python is not support direct method overloading. but we achive different way to method overloading in python.