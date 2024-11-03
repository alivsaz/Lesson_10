# Потоковая запись в файлы
import threading
import datetime
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for word in range(word_count):
            file.write(f'Какое-то слово № {word+1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time_function = datetime.datetime.today()
write_words(10, "example1.txt")
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time_function = datetime.datetime.today()

print(f'Работа потоков - {end_time_function - start_time_function}')

threadings = []
threadings.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threadings.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threadings.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threadings.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))
start_time_threading = datetime.datetime.today()
for threading in threadings:
    threading.start()
for threading in threadings:
    threading.join()
end_time_threading = datetime.datetime.today()

print(f'Работа потоков - {end_time_threading - start_time_threading}')