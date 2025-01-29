from collections import deque


def search(lines, pattern, history=5):
    prev_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prev_lines
        prev_lines.append(line)


if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prev_lines in search(f, 'python', 5):
            for prev in prev_lines:
                print(prev, end=' ')
            print(line, end=' ')
            print('-' * 20)
