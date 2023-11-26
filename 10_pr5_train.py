class Train:
    def __init__(self,name,fare,seates):
        self.name=name
        self.fare=fare
        self.seates=seates
    
    def getStetus(self):
        print(f"The name of the Train is {self.name}.")
        print(f"The available seates in the Train are {self.seates}.")
    
    def fareInfo(self):
        print(f"The price of ticket is : Rs. {self.fare}")

    def bookTicket(self):
        if(self.seates > 0):
            print(f"Your ticket has been booked! Your seat is {self.seates}")
            self.seates =self.seates - 1
        else:
            print("Sorry this train is fulll Kindly try in tatkal")

intercity=Train("Intercity Express: 14015",90,2)
intercity.getStetus()
intercity.bookTicket()
intercity.getStetus()
intercity.bookTicket()
intercity.getStetus()
intercity.bookTicket()
intercity.getStetus()