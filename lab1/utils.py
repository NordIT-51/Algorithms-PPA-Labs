import time
import psutil



def readfile():
    with open('input.txt', 'r') as file:
        s=file.readlines()
        return [line.strip() for line in s]

def writefile(info: str):
    with open('output.txt', 'w') as file:
        file.write(str(info))

def analyze(t_start, t_end):
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")

