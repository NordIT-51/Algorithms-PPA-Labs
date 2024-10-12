import time
import psutil

moves = {
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
    0: [4, 6]
}

def count_horsenumbers(n):
    if n == 1:
        return 8
    elif n <= 0:
        raise ValueError('n некорректно')
    dp = [0] * 10
    new_dp = [0] * 10

    # телефонный номер не может начинаться ни c цифры 0, ни с цифры 8.
    for num in range(10):
        if num in [0, 5, 8]:
            continue
        dp[num] = 1

    for _ in range(2, n + 1):
        for num in range(10):
            new_dp[num] = 0

        for num in range(10):
            if dp[num] == 0:
                continue
            for move in moves.get(num, []):
                new_dp[move] = (new_dp[move] + dp[num]) % 10**9

        dp, new_dp = new_dp, dp

    res = sum(dp) % 10**9
    return res

t_start = time.perf_counter()
with open('input17.txt', 'r') as fin:
    n = int(fin.read().strip())
    result = count_horsenumbers(n)
with open('output17.txt', 'w') as fout:
    fout.write(f"{result}\n")
t_end = time.perf_counter()
print(f"Время работы: {t_end - t_start:.8f} секунд.")
print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
