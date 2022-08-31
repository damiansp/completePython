import time


def light():
    time.sleep(0.001)

    
def medium():
    time.sleep(0.01)


def heavy():
    for _ in range(100):
        light()
        medium()
        medium()
    time.sleep(2)


def main():
    for _ in range(2):
        heavy()


if __name__ == '__main__':
    main()

    
