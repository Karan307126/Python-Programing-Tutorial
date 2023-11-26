class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __len__(self):
        return len(self.vec)

v1=Vector([1 , 4 , 4 , 1 ])
v2=Vector([3 , 5])
print(len(v1))
print(len(v2))