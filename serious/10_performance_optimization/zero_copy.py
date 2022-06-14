@profile
def read_random_poor():
    with open('./random.pkl', 'rb') as f:
        content = f.read(1024 * 10_000)
        to_do = content[1024:]
    print(f'Content length: {len(content)}\nto do: {len(to_do)}')
    with open('./rand_partial_copy.pkl', 'wb') as f:
        f.write(to_do)


@profile
def read_random():
    with open('./random.pkl', 'rb') as f:
        content = f.read(1024 * 10_000)
        to_do = memoryview(content)[1024:]
    print(f'Content length: {len(content)}\nto do: {len(to_do)}')
    with open('./rand_partial_copy.pkl', 'wb') as f:
        f.write(to_do)
        

if __name__ == '__main__':
    read_random_poor()
    read_random()
