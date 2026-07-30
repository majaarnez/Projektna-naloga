vsota_kvadratov = 0
for i in range(1, 101):
    vsota_kvadratov += i ** 2

kvadrat_vsote = 0
for i in range(1, 101):
    kvadrat_vsote += i

print (kvadrat_vsote ** 2 - vsota_kvadratov)