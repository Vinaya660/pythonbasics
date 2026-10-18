a= "I love pythgon"
print(a[::-1])
print(len(a))
print(a.count("o"))



text=input("enter the word")
reverse=text[::-1]
original =text
if reverse == original:
    print("palindrome")
else:
    print("not")