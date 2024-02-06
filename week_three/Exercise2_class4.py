try:
    text = []
    with open(r'mbox-short.txt', 'r') as file:
        for line in file:
            if 'From' in line and '2008' in line:
                text.append(line.split(' '))
    for i in range(len(text)):
        print('Sender: ' + text[i][1])


except:
    print('File dont exists')
    quit()