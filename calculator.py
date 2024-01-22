import math

print("Base: ")
base = int(input())

print("Exponent: ")
exponent = int(input())

print("Modulo: ")
modulo = int(input())

baseList = []
sum = 1

print()
print(f"{exponent} | {base}")
baseList.append(base)

while (exponent != 1):

    exponent = math.floor(exponent / 2)
    

    if (base*base) > modulo:
         baseBefore = base
         base = (base*base) % modulo
         print(f"{exponent} | {base} (= {baseBefore*baseBefore} mod {modulo})")
    else:
        base = (base*base)
        print(f"{exponent} | {base}")

    if exponent % 2 != 0:
        baseList.append(base)

for number in baseList:
    sum *= number

print()
print(f"{sum} mod {modulo}")
print(sum % modulo)