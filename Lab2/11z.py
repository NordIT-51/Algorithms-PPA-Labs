import bisect
import time
import psutil

def process(operations):
    elements = []
    results = []
    for line in operations:
        op, *args = line.strip().split()
        x = int(args[0]) if args else None

        if op == 'insert':
            idx = bisect.bisect_left(elements, x)
            if idx == len(elements) or elements[idx] != x:
                elements.insert(idx, x)
        elif op == 'delete':
            idx = bisect.bisect_left(elements, x)
            if idx < len(elements) and elements[idx] == x:
                elements.pop(idx)
        elif op == 'exists':
            idx = bisect.bisect_left(elements, x)
            results.append('true' if idx < len(elements) and elements[idx] == x else 'false')
        elif op == 'next':
            idx = bisect.bisect_right(elements, x)
            results.append(str(elements[idx]) if idx < len(elements) else 'none')
        elif op == 'prev':
            idx = bisect.bisect_left(elements, x)
            if idx > 0:
                results.append(str(elements[idx - 1]))
            else:
                results.append('none')

    return results

if __name__ == '__main__':
    t_start = time.perf_counter()
    with open('maxinput11.txt', 'r') as fin:
        operations = fin.readlines()
        results = process(operations)
    with open('output11.txt', 'w') as fout:
        for result in results:
            fout.write(result + '\n')
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")

