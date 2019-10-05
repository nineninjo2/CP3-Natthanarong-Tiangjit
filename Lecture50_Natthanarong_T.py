def d1 (a,s):
    print(a+s)
def d2(a, s):
    print(a-s)
def d3(a, s):
    print(a*s)
def d4(a, s):
    print(a/s)
end = 0
while end == 0 :
    a = int(input(">>>"))
    s = int(input(">>>"))
    m = (input("mark >>>"))
    if m == "+":
        d1(a,s)
        end =1
    elif m == "-":
        d2(a, s)
        end = 1
    elif m == "*":
        d3(a,s)
        end = 1
    elif m == "/":
        d4(a,s)
        end = 1
    else: print("ERRORR")
