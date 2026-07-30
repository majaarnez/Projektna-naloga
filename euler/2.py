a = 1
b = 2 #ker se zacne z 1 pa 2
vsota = 0
while a < 4000000:
    if a % 2 == 0:
        vsota += a
    a, b = b, a + b
print(vsota)