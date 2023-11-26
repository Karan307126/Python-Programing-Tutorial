class Laptop:
    def code(self, ide):
        ide.execute()

class Pycharm:
    def execute(self):
        print("Code run...")
        print("Debug code...")
        print("Spell check...")
        print("Code suggetion...")

class VS_Code:
    def execute(self):
        print("Code run...")
        print("Debug code...")

ide1 = Pycharm()
ide2 = VS_Code()
lap1 = Laptop()
lap2 = Laptop()
lap1.code(ide1)
print("\n")
lap2.code(ide2)