import time
import psutil


def find_approximate_matches(k, t, p):
    matches = []
    len_t = len(t)
    len_p = len(p)
    for i in range(len_t - len_p + 1):
        mismatch_count = sum(1 for j in range(len_p) if t[i + j] != p[j])
        if mismatch_count <= k:
            matches.append(i)
    return matches


def main():
    test_cases = []
    with open('input8.txt', 'r') as fin:
        lines = fin.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) < 3:
                continue
            k = int(parts[0])
            t = parts[1]
            p = parts[2]
            test_cases.append((k, t, p))
    all_matches = []
    for k, t, p in test_cases:
        matches = find_approximate_matches(k, t, p)
        all_matches.append(matches)

    with open('output8.txt', 'w') as fout:
        for matches in all_matches:
            if matches:
                output_line = f"{len(matches)} {' '.join(map(str, matches))}\n"
                fout.write(output_line)
            else:
                fout.write('0\n')



if __name__ == '__main__':
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")

