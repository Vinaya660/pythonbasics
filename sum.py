# num = int(input("Enter the number"))
# count = 0
# while num > 0:
#     num = num//10
#     count += 1

#     print("number of digits",count)


num = int(input("Enter the number"))
count = 0
while num > 0:
    digit = num%10
    count += digit
    num//=10

    print("sum of digits",count)


