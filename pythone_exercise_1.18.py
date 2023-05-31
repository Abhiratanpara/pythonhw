for i in range(0,5):
    # for j in range(0,i):
    #     print("*",end=" ")
    for k in reversed(range(0,i)):
        print("*",end=" ")
    print()
for i in reversed(range(0,5)):
    for j in reversed(range(0,i+1)):
        print("*",end=" ")
    print()