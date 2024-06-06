class Vehicle:
    vehicle_type = 'none'


class Car:
    price = 1000000

    def horse_powers(self):
        return 'Мощность: 250 л.с.'


class Nissan(Car, Vehicle):
    price = "Цена: 1500000"
    vehicle_type = 'Тип кузова: cедан'

    def horse_powers(self):
        print('Мощность: 300 л.с.')


nissan = Nissan()
print(nissan.vehicle_type)
print(nissan.price)
Nissan.horse_powers(nissan)
