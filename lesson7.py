#1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.

str_1_1 = [31, 22]
str_1_2 = [37, 43]
str_1_3 = [51, 86]
matr1 = [str_1_1, str_1_2, str_1_3]

str_2_1 = [3, 5, 32]
str_2_2 = [2, 4, 6]
str_2_3 = [-1, 64, -8]
matr2 = [str_2_1, str_2_2, str_2_3]

str_3_1 = [3, 5, 8, 3]
str_3_2 = [8, 3, 7, 1]
matr3 = [str_3_1, str_3_2]

str_4_1 = [31, 22, 11]
str_4_2 = [37, 43, 55]
str_4_3 = [51, 86, 23]
matr4 = [str_4_1, str_4_2, str_4_3]

class Matrix:
    def __init__(self, matr):
        self.matrix = matr
        
    def __str__(self):
        matrix_str=""
        for i in self.matrix:
            for j in i:
                matrix_str += f"{j:>4}"
            matrix_str += "\n"
        return matrix_str
    
    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return "Матрицы разного размера"
        num_strings = len(self.matrix)
        num_columns = len(self.matrix[0])
        new_matrix = []
        for i in range(num_strings):
            new_string = []
            for j in range(num_columns):
                new_string.append(self.matrix[i][j] + other.matrix[i][j])
            new_matrix.append(new_string)
        return Matrix(new_matrix) 
        
matrix_obj1 = Matrix(matr1)
print(matrix_obj1)

matrix_obj2 = Matrix(matr2)
print(matrix_obj2)

matrix_obj3 = Matrix(matr3)
print(matrix_obj3)

matrix_obj4 = Matrix(matr4)
print(matrix_obj4)

print(matrix_obj2 + matrix_obj4)

matrix_obj5 = matrix_obj2 + matrix_obj4

print(matrix_obj5)


#2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. 

from abc import ABC, abstractmethod

class Clothes(ABC):
       
    @abstractmethod
    def amount_textile(self):
        pass
    
class Coat(Clothes):
    def __init__(self, size):
        self.v = size
        
    @property
    def amount_textile(self):
        return (self.v / 6.5 + 0.5)
    
class Suit(Clothes):
    def __init__(self, size):
        self.h = size
    
    @property
    def amount_textile(self):
        return (2 * self.h + 0.3)

class Textile():
    
    def __init__(self):
        self.clothes_list = []
        
    def add_clothes(self, title, size):
        if title == "coat":
            self.clothes_list.append(Coat(size).amount_textile)
        elif title == "suit":
            self.clothes_list.append(Suit(size).amount_textile)
        else:
            print("Такого предмета одежды нет в базе!")
    
    def total_amount_textile(self):
        total_amount = 0
        for el in self.clothes_list:
            total_amount += el
        return total_amount

ct = Coat(52)
print("Для пальто требуется ткани - ", ct.amount_textile)

st = Suit(1.8)
print("Для костюма требуется ткани - ", st.amount_textile)

cl = Textile()
cl.add_clothes("coat", 52)
cl.add_clothes("coat", 48)
cl.add_clothes("suit", 1.5)
cl.add_clothes("suit", 1.7)
print("Для всей одежды требуется ткани - ", round(cl.total_amount_textile(),2))
    
#3. Реализовать программу работы с органическими клетками, состоящими из ячеек. 

class Cell:
    def __init__(self, amount):
        self.amount = amount
    
    def __add__(self, other):
        return Cell(self.amount + other.amount)
    
    def __sub__(self, other):
        if self.amount > other.amount:
            return Cell(self.amount - other.amount)
        else:
            print("Операция невозможна! Разность двух клеток меньше нуля!")
            return None
            
    def __mul__(self, other):
        return Cell(self.amount * other.amount)
            
    def __truediv__(self, other):
        res = round(self.amount / other.amount)
        if res != 0:
            return Cell(res)
        else:
            print("Операция невозможна! Результат деления двух клеток равен нулю!")
            return None

    def make_order(self, row):
        str = ""
        for i in range(self.amount // row):
            str += "*" * row + "\n"
        if self.amount % row == 0:
            str = str[:-1]
        else:
            str += "*" * (self.amount % row)
        return str

c0 = Cell(3)
c1 = Cell(5)
c2 = Cell(7)

print(c0.make_order(5))
print("-"*20)
print(c1.make_order(5))
print("-"*20)
print(c2.make_order(5))
print("-"*20)

c3 = c1 + c2
print(c3.make_order(5))
print("-"*20)

print((c0 + c1).make_order(5))
print("-"*20)

print((c0 * c1).make_order(5))
print("-"*20)

if c3 - c0 != None:
    print((c3 - c0).make_order(5))
print("-"*20)

if c0 - c3 != None:
    print((c0 - c3).make_order(5))
print("-"*20)

c5 = c2 / c1
if c5 != None:
    print(c5.make_order(5))
print("-"*20)

if c3 / c0 != None:
    print((c3 / c0).make_order(5))
print("-"*20)

if c0 / c2 != None:
    print((c0 / c2).make_order(5))
print("-"*20)




