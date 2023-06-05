

def prim(n,l=[],div=2):
    if n == 1:
        return l
    
    if n %div == 0:
        n = n/div
        l.append(div)
        
    else:
        div += 1

    return prim(n,l,div)
    


n = 660

primos = []

div = 2
while n != 1:
    if n %div == 0:
        n = n/div
        primos.append(div)
    else:
        div += 1
n = 660
print(primos)
print(prim(n))