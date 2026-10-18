# for i in range(1,6):
#     for j in range(i):
#         print("#", end="")
#     print()



num=int(input("enter anumber"))
original=num
reverse = 0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if original==reverse:
        print("palindrime")
else:
        print("not palimdrome")