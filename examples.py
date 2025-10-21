# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#
#     def drive(self):
#         print(f"{self.brand} {self.color} is moving")
#
# car1 = Car("Toyota", "red")
# car2 = Car("BMW", "black")
# car3 = Car("Mercedes", "White")
#
# car1.drive()
# car2.drive()
# car3.drive()



# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower
#         self.is_running = False
#
#     def start(self):
#         self.is_running = True
#         print(f"Engine with horsepower {self.horsepower} started.")
#
#     def stop(self):
#         self.is_running = False
#         print(f"Engine with horsepower {self.horsepower} stopped.")
#
# class Car:
#     def __init__(self, brand, engine):
#         self.brand = brand
#         self.engine = engine
#
#     def drive(self):
#         if not self.engine.is_running:
#             print("I cant drive - the engine has not start working")
#         else:
#             print(f"{self.brand} is driving forward")
#
#     def start_engine(self):
#         self.engine.start()
#
# class Person:
#     def __init__(self, name, car):
#        self.name = name
#        self.car = car
#
#     def go_to_work(self):
#         print(f"{self.name} is about to go to work")
#         self.car.start_engine()
#         self.car.drive()
#
# engine = Engine(150)
# car = Car("BMW", engine)
# person = Person("Tedi", car)
#
# person.go_to_work()



class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def drive(self):
        print(f"The {self.color} car is driving.")

    def info(self):
        print(f"This car is a {self.color} {self.brand} car.")

car1 = Car("black", "BMW")
# car2 = Car("blue")
# car3 = Car("green")
# car4 = Car("cyan")
#
car1.drive()
car1.info()
# car2.drive()
# car3.drive()
# car4.drive()

