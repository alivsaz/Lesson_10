# Блокировки и обработка ошибок
import threading
from random import randint
from time import sleep

class Bank:
    balance = 0
    lock = threading.Lock()

    def deposit(self):
        count = 100
        while count > 0:
            deposits = randint(50, 500)
            self.balance += deposits
            print(f'Пополнение: {deposits}. Баланс: {self.balance}')
            count -= 1
            sleep(0.001)
            if self.balance >500 and self.lock.locked():
                self.lock.release()

    def take(self):
        count = 100
        while count > 0:
            takes = randint(50, 500)
            print(f'Запрос на {takes}')
            if takes <= self.balance:
                self.balance -= takes
                print(f'Снятие: {takes}. Баланс: {self.balance}')
                count -= 1
                sleep(0.001)
            else:
                print('Запрос отклонён, недостаточно средств')
                if not self.lock.locked():
                    self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')