from random import randint as rnt, choice as chs, random


ALPHABET = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper()
NUMS = '0123456789'
E = 2.718281828459045


def Search(List, element): #Берёт на вход список/строку и значение, выводит значение, если оно есть в списке/строке
    if element in List:
        return(element)
    else:
        return()
    
def Factorial(num): #На вход берёт int на выходе получается факториал данного int числа 
    if num == 0:
        return 1
    else:
        return num * Factorial(num-1)
    
def Subfactorial(num):
    return round(Factorial(num)/E)

def Cut(List, count): #На вход берёт список и int n, на выходе получаем список с n случайными элементами данного списка
    res = []
    for i in range(count):
        res.append(chs(List))
    return(res)

def Reverse(List): #На вход берёт список/строку, на выходе возвращает отзеркаленную версию
    return(List[::-1])

def AllSum(num): #Находит треугольное число, данного числа   int -> int
    return sum(range(num))

def Round(flt): #Округляет число до целого   float -> int
    if type(flt) == float:
        add = 0
        flt = str(flt)
        for i in range(len(flt)):
            if flt[i] == ".":
                _id = i
        flt = list(flt)
        if int(flt[_id+1]) > 4:
            add = 1
        for i in range(len(flt)-1, -1, -1):
            if flt[i] != ".":
                flt.pop(i)
            else:
                flt.pop(i)
                break
        result = ''
        for i in range(len(flt)):
            result += flt[i]
        result = int(result) + add
        return(int(result))
    elif type(flt) == int:
        return(flt)
    
def Binar(num): #Переводит число в двоичную систему счисления   int -> int
    binar = ''
    while num != 1:
        binar += str(num%2)
        num = num//2
    binar += '1'
    return(Reverse(binar))

def Divisibility(num, div): #Проверяет делимость числа на другое число   int, int -> bool
    if (type(num) and type(div)) == int:
        if num%div == 0:
            return(True)
        else:
            return(False)
    else:
        return(None)
    
def ManageStr(var): #Выводит в консоль количество каких-либо букв в строке   str -> None
    if type(var) == str:
        var = var.upper()
        manage = str()
        for letter in ALPHABET:
            count = len(var) - len(var.replace(letter, ""))
            manage += ("\n" + letter + ": " + str(count))
        print("Lenght: " + str(len(var)) + manage)

class switch(): #Сменная переменная в виде списка
    def __init__(self, lst):
        self.lst = lst
        self.enable = 0

    def read(self):
        print(self.lst)
        print(self.enable)
        return()

    def move(self, amount):
        self.enable += amount
        return()
    
    def get(self):
        return(self.lst[self.enable])
    
    def clean(self):
        self.lst = []
        return()
    
    def change(self, index):
        self.enable = (index)%len(self.lst)
        return()
    
    def update(self, element):
        if not (element in self.lst):
            self.lst.append(element)
        self.enable = self.lst.index(element)
        return()

    def erase(self, element):
        if element in self.lst:
            self.lst.remove(element)
        return()
    
    def delete(self, index):
        self.enable = index%len(self.lst)
        element = self.lst[index]
        self.lst.remove(element)
        return()
    
    def slise(self, _index, index_):
        return(self.lst[_index:index_])
    
    def add(self, element):
        self.lst.append(element)
        return()
    
class hexadecimal(): #Число в шестнадцатиричной системе счисления
    def __init__(self, num:str):
        self.num = num
        return
    
    def decimal(self):
        num = int()
        for i in range(len(self.num)):
            if self.num[i] in NUMS:
                num += int(self.num[i]) * 16**(len(self.num) - (i+1))
            else:
                pass

        


def chance(chance:float) -> bool: #Высчитывает выпало/не выпало по шансу   int -> bool
    if chance > 1:
        return None
    a = random()
    if a <= chance:
        return True
    else:
        return False

def locateId(list, index): #Возвращает значение из списка по индексу если такой существует
    if len(list) > index:
        return list[index]
    
def Multiply(NUMS:list):
    result = 1
    for number in NUMS:
        result *= number
    return result

def AverageArephmetic(NUMS:list):
    return round(sum(NUMS)/len(NUMS), 2)

def AverageGeometric(NUMS:list): #Возвращает среднее геометрическое числового ряда
    for num in NUMS:
        num **= 2
    return round(Multiply(NUMS)**(1/len(NUMS)), 2)

def Dispersion(NUMS:list): #Возвращает дисперсию числового ряда
    average = AverageArephmetic(NUMS)
    for num in NUMS:
        num -= average
        print(num)
        num **= 2
        print(num)
    return round(AverageArephmetic(NUMS), 2)
