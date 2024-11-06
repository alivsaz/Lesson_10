# Многопроцессное считывание
import datetime
from multiprocessing.pool import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        string = file.readline()
        all_data.append(string)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start_time = datetime.datetime.today()
# for filename in filenames:
#     read_info(filename)
# end_time = datetime.datetime.today()
# print('Линейный вызов. Время выполнения: ', end_time - start_time)

if __name__ == '__main__':
     start_time = datetime.datetime.today()

     with Pool(4) as pool:
         pool.map(read_info, filenames)

     end_time = datetime.datetime.today()
     print('Многопроцессный. Время выполнения: ', end_time - start_time)