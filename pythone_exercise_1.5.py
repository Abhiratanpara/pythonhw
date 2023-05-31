numbers = [12, 25, 150, 188, 145, 525, 500]

for i in numbers:
    if i%5 == 0:
        if i > 150:
            continue
        elif i>500:
            break
        print(i)