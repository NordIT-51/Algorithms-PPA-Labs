import time
import psutil


def do_the_Alchemy():
    p = []
    a = []

    def GetID(name):
        for i in range(len(p)):
            if p[i] == name:
                return i
        p.append(name)
        for row in a:
            row.append(0)
        a.append([0] * len(p))
        return len(p) - 1

    with open('input11.txt', 'r') as file:
        lines = file.readlines()

    m = int(lines[0].strip())
    for line in lines[1:m + 1]:
        src_dest = line.strip().split('->')
        src = src_dest[0].strip()
        dest = src_dest[1].strip()
        src_id = GetID(src)
        dest_id = GetID(dest)
        a[src_id][dest_id] = 1

    start = lines[m + 1].strip()
    target = lines[m + 2].strip()
    start_id = GetID(start)
    target_id = GetID(target)

    n = len(p)
    d = [0] * n
    d[start_id] = 1

    for k in range(1, n):
        for i in range(n):
            if d[i] == k:
                for j in range(n):
                    if a[i][j] == 1 and d[j] == 0:
                        d[j] = k + 1

    if d[target_id] == 0:
        result = -1
    else:
        result = d[target_id] - 1

    with open('output11.txt', 'w') as file:
        file.write(f"{result}\n")


if __name__ == "__main__":
    t_start = time.perf_counter()
    do_the_Alchemy()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
