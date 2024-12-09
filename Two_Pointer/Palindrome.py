str = "racecar....".lower()

p1 = 0
p2 = len(str) - 1

for char in str:
    if char.isalnum():
        print("it is alnum: ", char)
    else:
        print("not: ", char)


while p1 < p2:

    while not (str[p1].isalnum()):
        p1+=1

    while not (str[p2].isalnum()):
        p2-=1

    if str[p1] != str[p2]:
        print("Not palindrome")
        break
    else:
        p1+=1
        p2-=1

else:
    print("palindrome")