import time
import psutil


def find_substrings(p, t):
    occurrences = []
    p_len = len(p)
    for i in range(len(t) - p_len + 1):
        if t[i:i + p_len] == p:
            occurrences.append(i + 1)
    return occurrences

def main():
    with open('mininput1.txt', 'r') as file:
        p = file.readline().strip()
        t = file.readline().strip()
    occurrences = find_substrings(p, t)
    with open('output1.txt', 'w') as file:
        file.write(f"{len(occurrences)}\n")
        if occurrences:
            file.write(" ".join(map(str, occurrences)) + "\n")

if __name__ == "__main__":
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
