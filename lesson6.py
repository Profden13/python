#1. Создать класс TrafficLight (светофор).

import time

class TrafficLight:
    __color = "" 
    def running(self):
        color = "красный"
        print("Светофор красный")
        time.sleep(7)
        color = "желтый"
        print("Светофор желтый")
        time.sleep(2)
        color = "зеленый"
        print("Светофор зеленый")
        time.sleep(7)
        color = ""
        
tl = TrafficLight()
tl.running()

#2. Реализовать класс Road (дорога).

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    def road_amount_asphalt(self):
        self.thickness = 5
        self.amount_asphalt_1m = 25
        return self._length * self._width * self.thickness * self.amount_asphalt_1m

rd = Road(5000, 20)
rd.road_amount_asphalt()
        
#3. Реализовать базовый класс Worker (работник).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
    
class Position(Worker):
   
    def get_full_name(self):
        return self.surname + " " + self.name
    
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

position1 = Position("Сергей", "Иванов", "програмист", 50000, 20000)   
print(position1.get_full_name()) 
print(position1.get_total_income()) 
print(position1.name)
print(position1.surname)
print(position1.position)
print(position1._income)
print(position1._income['wage'])
print(position1._income['bonus'])

position2 = Position("Алексей", "Петров", "дизайнер", 60000, 15000)   
print(position2.get_full_name()) 
print(position2.get_total_income()) 
print(position2.name)
print(position2.surname)
print(position2.position)
print(position2._income)
print(position2._income['wage'])
print(position2._income['bonus'])    
    
#4. Реализуйте базовый класс Car.   

class Car:
    
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        
    def go(self):
        print("Машина поехала")
        
    def stop(self):
        print("Машина остановилась")
        
    def turn(self, direction):
        print("Машина повернула " + direction)
    
    def show_speed(self):
        print(f"Текущая скорость машины - {self.speed} км/ч")

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
    
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Внимание!!! Превышение скорости!!!")

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        
class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Внимание!!! Превышение скорости!!!")
        
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

auto1 = Car(80, "white", "Mercedes C200", False)
print(f"1 машина - {auto1.name}, цвет - {auto1.color}.")
if auto1.is_police: 
    print('Полицейская машина')
auto1.go()
auto1.turn("налево")
auto1.show_speed()
auto1.turn("направо")
auto1.stop()

print("-"*40)

auto2 = TownCar(80, "black", "BMW 5")
print(f"2 машина - {auto2.name}, цвет - {auto2.color}.")
if auto2.is_police: 
    print('Полицейская машина')
auto2.go()
auto2.turn("налево")
auto2.show_speed()
auto2.turn("направо")
auto2.stop()

print("-"*40)

auto3 = SportCar(120, "red", "Ferrari")
print(f"3 машина - {auto3.name}, цвет - {auto3.color}.")
if auto3.is_police: 
    print('Полицейская машина')
auto3.go()
auto3.turn("налево")
auto3.show_speed()
auto3.turn("направо")
auto3.stop()

print("-"*40)

auto4 = WorkCar(50, "yellow", "Man")
print(f"4 машина - {auto4.name}, цвет - {auto4.color}.")
if auto2.is_police: 
    print('Полицейская машина')
auto4.go()
auto4.turn("налево")
auto4.show_speed()
auto4.turn("направо")
auto4.stop()

print("-"*40)

auto5 = PoliceCar(100, "white", "Ford")
print(f"5 машина - {auto5.name}, цвет - {auto5.color}.")
if auto5.is_police: 
    print('Полицейская машина')
auto5.go()
auto5.turn("налево")
auto5.show_speed()
auto5.turn("направо")
auto5.stop()

#5. Реализовать класс Stationery (канцелярская принадлежность).

class Stationery:
    def __init__(self, title):
        self.title = title
        
    def draw(self):
        print("Запуск отрисовки")
        
class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationery):
    
    def draw(self):
        print("Запуск отрисовки карандашом")

class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки маркером")

st1 = Stationery("канцелярская принадлежность")
st1.draw()
print(st1.title)

st2 = Pen("ручка")
st2.draw()
print(st2.title)

st3 = Pencil("карандаш")
st3.draw()
print(st3.title)

st4 = Handle("маркер")
st4.draw()
print(st4.title)


