# За честь и отвагу!
import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy, count = 100, 0
        while enemy > 0:
            enemy -= self.power
            count += 1
            sleep(1)
            print(f'{self.name} сражается {count} дней, осталось {enemy} воинов.')
        print(f'{self.name} одержал победу спустя {count} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

for knight in (first_knight, second_knight):
    if first_knight.is_alive() and second_knight.is_alive():
        knight.join()

print('Все битвы закончились!')