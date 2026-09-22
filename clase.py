def MCD (a,b): 
    print(f"a={a} - b={b}") 
    res= a
    while (b != 0):
        res= MCD (b, a % b)
        a = b
        b = a % b
    return res
print(MCD(48, 18))
