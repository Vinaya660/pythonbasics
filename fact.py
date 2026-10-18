# num=int(input("enter a number"))
# fact=1
# for i in range(1,num+1):
#         fact*=i
# print(fact)



num=int(input("Enter anumber"))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//1
    print(reverse)
