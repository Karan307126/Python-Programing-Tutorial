class RailwayForm:
    formtype="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

karanApplication=RailwayForm()
karanApplication.name="Karan"
karanApplication.train="Rajdhani Express"
karanApplication.printData()