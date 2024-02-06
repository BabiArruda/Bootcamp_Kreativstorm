try:
    with open(r'test.txt', 'r') as test:
        text = test.read().strip('\n').upper()
    print(text)
except:
    print('File dont exists')