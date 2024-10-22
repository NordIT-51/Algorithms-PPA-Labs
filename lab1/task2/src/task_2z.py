import time
import psutil
from utils import readfile, writefile, analyze


def calculate_refuels(d, m, stops):
    stops.append(d)
    refill_num = 0
    pos = 0
    reach = m
    i = 0
    while pos < d:
        if reach >= d:
            break
        last_pos = pos
        while i < len(stops) and stops[i] <= reach:
            last_pos = stops[i]
            i += 1
        if last_pos == pos:
            return -1
        refill_num += 1
        pos = last_pos
        reach = pos + m
    return refill_num

if __name__ == "__main__":
    t_start = time.perf_counter()
    inp = readfile()
    d,t,n = int(inp[0].strip()), int(inp[1].strip()), int(inp[2].strip())
    stops = list(map(int, inp[3].strip().split()))
    writefile(str(calculate_refuels(d, t, stops)) + '\n')
    t_end = time.perf_counter()
    analyze(t_start, t_end)


