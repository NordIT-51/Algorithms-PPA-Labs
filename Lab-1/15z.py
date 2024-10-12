import time
import psutil

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
    with open("input15.txt", "r") as infile:
        s = infile.read().strip()
    with open("output15.txt", "w") as outfile:
        outfile.write(repair_brackets(s))
    t_end = time.perf_counter()
print(f"Время работы: {t_end - t_start:.8f} секунд.")
print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
