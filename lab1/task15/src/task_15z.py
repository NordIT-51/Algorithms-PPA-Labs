import time
import psutil
from utils import readfile, writefile, analyze


def isMatching(char1, char2):
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return pairs[char1] == char2


def repair_brackets(s):
    stack = []
    to_remove = set()
    for i, c in enumerate(s):
        if c in '({[':
            stack.append(i)
        elif c in ')}]':
            if stack and isMatching(c, s[stack[-1]]):
                stack.pop()
            else:
                to_remove.add(i)

    while stack:
        to_remove.add(stack.pop())

    return ''.join([s[i] for i in range(len(s)) if i not in to_remove])

if __name__ == "__main__":
    t_start = time.perf_counter()
    inp = readfile()
    s = inp[0].strip()
    writefile(repair_brackets(s))
    t_end = time.perf_counter()
    analyze(t_start, t_end)