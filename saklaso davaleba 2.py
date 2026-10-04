L = [1,2,3,4,5,6,7,8,9,10]
total = 0
def jami():
    global total
    for i in L:
        total += i
    print(total)

jami()