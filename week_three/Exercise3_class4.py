try:
    text = {}
    temp_list = []
    with open(r"week_three/sender.txt", "r") as file:
        for line in file:
            email = line.replace("Sender: ", "").rstrip("\n")
            temp_list.append(email)
            if not email in text:
                text[email] = 1
            else:
                text[email] += 1

    print(text)


except:
    print("File dont exists")
    quit()
