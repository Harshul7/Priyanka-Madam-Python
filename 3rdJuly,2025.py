'''
    A
   / \
  /   \
  B   C
 /    /
D    /
\   /
 \ /
  E

'''
class A:
    def __init__(self,name,place):
        print("in Class A")
        self.name=name
        self.place=place
    
    def __str__(self):
        return f"A={self.name} and place of A={self.place}"

class B(A):
    def __init__(self,name,place):
        print("in Class B")
        super().__init__(name,place)

class C(A):
    def __init__(self,name,place,animal):
        print("in Class C")
        super().__init__(name,place)
        self.animal=animal

class D(B):
    def __init__(self,name,animal):
        print("in Class D")
        super().__init__(name,animal)
        self.animal=animal

class E(D,C):
    def __init__(self,name):
        print("in Class E")
        super().__init__(name)

A1=A("Ranbir Kapoor","Mumbai")
C1=C("","","Animal")
print(C1.animal)
print(C1)

D1=D("Ranbir Kapoor","Animal")
print(D1)


        