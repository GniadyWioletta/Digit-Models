import random

generated = []
line = []

for i in range(20):
    line = []
    text = ""
    j = 0
    while j < 4:
        number = random.randint(0, 21)
        if number not in line:
            line.append(number)
            text += str(number) + " "
            j = j+1

    with open("test_series.txt", mode='a') as file:
            file.write(text + "\n")
