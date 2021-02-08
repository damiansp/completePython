def tryparse(string, base=10):
    try:
        return int(string, base=base)
    except ValueError:
        return None


def main():
    for val in ['123', 'abc']:
        if (n := tryparse(val)) is not None:
            print(n) # 123
        print(10 * (n if (n := tryparse(val)) is not None else 1)) # 1230, 10

    print(10 * tryparse('10'))     # 10
    print(10 * tryparse('0a', 16)) # 100
    
          
    
main()
