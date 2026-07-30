stevilo = 2 ** 1000
vsota = 0
while stevilo > 0:
    vsota += stevilo % 10
    stevilo = stevilo // 10

print(vsota)