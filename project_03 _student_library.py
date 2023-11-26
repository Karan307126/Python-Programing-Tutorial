class Librery:

    def __init__(self,listOfBooks):
        self.books=listOfBooks

    def displayAvailableBooks(self):
        print("Bookspresent in this librery are: ")
        for book in self.books:
            print("\t * " + book)


class Student:
    def __init__(self, Name, EnrNo):
        self.Name = Name
        self.EnrNo = EnrNo
    
    def studentInfo(self):
        print(f"Student name is {self.Name}.")
        print(f"Student Enrollment No is {self.EnrNo}.")
        

if __name__ == "__main__":
    centrelLibrery = Librery(["Algorithms","Django","Clrs","Python Notes"])
    centrelLibrery.displayAvailableBooks()
    s1 = Student("Karan", 200280107036)
    s1.studentInfo()