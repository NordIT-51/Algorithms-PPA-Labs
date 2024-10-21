import time
import psutil


def binary_insert(items, k):
    low = 0
    high = len(items)
    while low < high:
        mid = (low + high) // 2
        if items[mid] < k:
            low = mid + 1
        else:
            high = mid
    items.insert(low, k)

def binary_remove(items, k):
    low = 0
    high = len(items)
    while low < high:
        mid = (low + high) // 2
        if items[mid] < k:
            low = mid + 1
        else:
            high = mid
    if low < len(items) and items[low] == k:
        items.pop(low)

def main():
    with open("input16.txt", "r") as fin, open("output16.txt", "w") as fout:
        n = int(fin.readline().strip())
        items = []
        for i in range(n):
            line = fin.readline().strip()
            if not line:
                continue
            command, k = map(int, line.split())

            if command == 1: # Добавление
                low = 0
                high = len(items)
                isDuplicate = False
                while low < high:
                    mid = (low + high) // 2
                    if items[mid] == k:
                        isDuplicate = True
                        break
                    elif items[mid] < k:
                        low = mid + 1
                    else:
                        high = mid
                if not isDuplicate:
                    binary_insert(items, k)
            elif command == 0: # Вывод
                if 0 < k <= len(items):
                    kth_maximum = items[-k]
                    fout.write(str(kth_maximum) + "\n")
                else:
                    fout.write("Error: Not enough items\n")
            elif command == -1: # Удаление
                binary_remove(items, k)

if __name__ == "__main__":
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
