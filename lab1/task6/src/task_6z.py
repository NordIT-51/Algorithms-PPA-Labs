import time
import psutil
from utils import readfile, writefile, analyze

def maxnum(nums):
    nums = [str(num) for num in nums]
    maxlen = max(len(x) for x in nums)
    nums.sort(key=lambda x: x * (maxlen * 2), reverse=True)
    res = ''.join(nums)
    return '0' if res.lstrip('0') == '' else res


if __name__ == "__main__":
    t_start = time.perf_counter()
    inp = readfile()
    n = inp[0]
    nums = inp[1].split()
    writefile(maxnum(nums))
    t_end = time.perf_counter()
    analyze(t_start, t_end)