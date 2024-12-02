import hashlib

input = b'bgvyzdsv'

i = 1
while True:
    result = hashlib.md5(input + bytes(str(i), 'utf-8'))
    if result.hexdigest()[:5] == '00000':
        print(result.hexdigest())
        print(i)
        break
    else:
        i += 1
