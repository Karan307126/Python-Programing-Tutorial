class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

v1=Vector([6 , 4 , 3]) 
v2=Vector([7 , 5 , 9])
print(v1)
print(v2)