import pickle

class Car:
    def __init__(self, model, color, number):
        self.model = model.upper()
        self.color = color.upper()
        self.number = number.upper()

    def __str__(self):
        return f'Модель: {self.model}, цвет: {self.color}, г-н: {self.number} '

class Parking:
    def __init__(self):
        self.parking = {}
        with open('parking.ini', 'rb') as sd:
            self.parking = pickle.load(sd)
        print('Чтение данных...')

    def savedata(self):
        with open('parking.ini', 'wb') as sd:
            pickle.dump(self.parking, sd)
        print('Сохранение данных...')

    def getcar(self, row=0, place=0):
        if row == 0:
            return dict(filter(lambda x: x[0][0], self.parking.items()))
        elif place == 0:
            return dict(filter(lambda x: x[0][0] == row, self.parking.items()))
        else:
            return dict(filter(lambda x: (x[0][0] == row) and (x[0][1] == place), self.parking.items()))

def listparking(cars):
    for place, car in sorted(cars.items()):
        print(f'ROW - {place[0]} PLACE - {place[1]}; {car}')

def addcar():
    row = int(input('Ряд ===> '))
    place = int(input('Место ===> '))
    if parking.getcar(row, place) == {}:
        model = input('Модель: ')
        color = input('Цвет: ')
        number = input('Номер:')
        parking.parking[(row, place)] = Car(model, color, number)
    else:
        print('Место занято ...')

def delcar():
    row = int(input('Ряд ===> '))
    place = int(input('Место ===> '))
    if parking.getcar(row, place) != {}:
        del parking.parking[(row, place)]

def editcar():
    row = int(input('Ряд ===> '))
    place = int(input('Место ===> '))
    car = parking.parking[(row, place)]
    print(f'CAR: {car.model} {car.color} {car.number}')
    model = input('Модель: ')
    color = input('Цвет: ')
    number = input('Номер:')
    parking.parking[(row, place)] = Car(model, color, number)

menustr = 'a - add; d - del; e - edit; l - list; lr - list row; la - list all; q - quit; ===>'

parking = Parking()
# print(parking.getcar())

while True:
    choice = input(menustr)
    if choice == 'a':
        addcar()
    elif choice == 'd':
        delcar()
    elif choice == 'e':
        editcar()
    elif choice == 'l':
        row = int(input('Ряд ===> '))
        place = int(input('Место ===> '))
        listparking(parking.getcar(row, place))
    elif choice == 'lr':
        row = int(input('Ряд ===> '))
        listparking(parking.getcar(row))
    elif choice == 'la':
        listparking(parking.getcar())
    elif choice == 'q':
        parking.savedata()
        print('Конец работы ...')
        break
    else:
        print('Неверный выбор ...')
        continue
