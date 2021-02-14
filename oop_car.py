class car :
   speed = 0
   color=""


   def speeding(self):
     if self.speed <=50:
        print("your speed is less then 50 ")
        self.speed = self.speed + 10

     elif self.speed >50:
        print("your speed is over 50 slow down !!" )

        self.speed = self.speed - 20


   def carColor(self):
        self.color= self.color



x =car()
x.speed=20
x.color="red"
x.speeding()
x.carColor()
print("car speed is",x.speed,",car color is",x.color)

y =car()
y.speed=60
y.color="black"
y.speeding()
y.carColor()
print("car speed is",y.speed,",car color is",y.color)


z =car()
z.speed=80
z.color="white"
z.speeding()
z.carColor()
print("car speed is",z.speed,",car color is",z.color)
