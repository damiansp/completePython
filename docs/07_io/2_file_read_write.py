import json


# 1. File Obj Methods
with open('test.txt', 'r') as f:
    print('1:', f.read()) # prints whole file
    print('2:', f.read()) # ''

with open('test.txt', 'r') as f:
    for i, line in enumerate(f):
        print(f'{i + 1}: {line}')

with open('test2.txt', 'w') as f:
    f.write('Just another test\n')
        
f = open('test3.txt', 'rb+')
f.write(b'0123456789abcdef') # 16
f.seek(5)                    # go to 6th byte in file
print(f.read(1))             # b'5'
f.seek(-3, 2)                # go to 3rd byte before end
print(f.read(1))             # b'd'


# json
json_obj = [1, 'simple', 'list']
print(json.dumps(json_obj))
with open('test.json', 'w') as f:
    json.dump(json_obj, f)

with open('test.json', 'r') as f:
    x = json.load(f)
print(x)

    
