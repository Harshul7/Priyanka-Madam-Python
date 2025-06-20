class Car:
    def __init__(self,name,max_speed):
        self.name=name
        self.max_speed=max_speed 
    
    def getName(self):
        return self.name 
    
    def getMaxSpeed(self):
        return self.max_speed
    
    def setName(self,name):
        self.name=name
    
    def setMaxSpeed(self,max_speed):
        self.max_speed=max_speed


car1=Car("Lamborghini",400)
car2=Car("Maruti Suzuki",180)
car3=Car("Benz",250)

print(car1)
print(car2)
print(car1.max_speed)

print(car1.getMaxSpeed())
print(car2.getName())
print(car3.getName()," ",car3.getMaxSpeed())

car1.setName("Harshul")
print(car1.getName())

car1.setMaxSpeed(300)
print("car1.getMaxSpeed()=",car1.getMaxSpeed())


 