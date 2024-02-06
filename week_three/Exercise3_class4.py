try:
    text = {}
    temp_list = []
    with open(r'sender.txt', 'r') as file:
        for line in file:
            email = line.replace('Sender: ', '')
            temp_list.append(email)

        for i in range(len(temp_list)):
        x = text_read.count(email)
        print(email, temp, end='')



except:
    print('File dont exists')
    quit()