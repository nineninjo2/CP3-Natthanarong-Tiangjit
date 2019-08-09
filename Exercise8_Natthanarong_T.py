u = input("Username : ")
p = input("Password : ")
if u == "nine" and p == "nonono" :
    print("----------nineshop---------")
    print("cat 10 THB")
    print("dog 15 THB")
    print("pig 20 THB")
    s = input(">>>>>")
    if s == "cat" :
        h = int(input("howmany : "))
        print("Total : ",int(h*10),"THB")
    elif s == "dog" :
        h = int(input("howmany : "))
        print("Total : ",int(h*15),"THB")
    elif s == "pig" :
        h = int(input("howmany : "))
        print("Total : ",int(h*20),"THB")
    else :
        print("ERROR!!!!!!")
else :
    print("ERROR!!!!!!")
