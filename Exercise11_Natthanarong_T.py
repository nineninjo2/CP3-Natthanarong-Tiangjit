num = int(input())
g = 0
for x in range(num):
    g += 1
    print((num-g)*" "+(2*(x+1)-1)*"*")
