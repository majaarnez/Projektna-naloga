def fakulteta(n):
    if n == 0:
        return 1
    else:
        return n * fakulteta(n - 1)
    
stevilo = fakulteta(100)

vsota = 0
while stevilo > 0:
    vsota += stevilo % 10
    stevilo = stevilo // 10

print(vsota)