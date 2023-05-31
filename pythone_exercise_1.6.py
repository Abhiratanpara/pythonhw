number = int(input("enter number: "))
count = 0

# this code is not run
# for i in number:
#     i //= 10
#     count+=1

while number > 0:
    number //= 10
    count += 1
print("Total number in this Number is :",count)