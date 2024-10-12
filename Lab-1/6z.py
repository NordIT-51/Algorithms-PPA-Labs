import time
import psutil


def maxnum(nums):
    nums = [str(num) for num in nums]
    maxlen = max(len(x) for x in nums)
    nums.sort(key=lambda x: x * (maxlen * 2), reverse=True)
    res = ''.join(nums)
    return '0' if res.lstrip('0') == '' else res


if __name__ == "__main__":
    t_start = time.perf_counter()
    with open('input6.txt', 'r') as file:
        n = int(file.readline().strip())
        nums = list(map(int, file.readline().strip().split()))
    with open('output6.txt', 'w') as file:
        file.write(maxnum(nums))
    t_end = time.perf_counter()

print(f"Время работы: {t_end - t_start:.8f} секунд.")
print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
