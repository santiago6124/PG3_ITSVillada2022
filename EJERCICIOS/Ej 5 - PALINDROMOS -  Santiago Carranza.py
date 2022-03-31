def esCapicua(s):
    return s == s[::-1]


s = input("Ingrese una palabra: ")
ans = esCapicua(s)

if ans:
    print("La palabra ", s, " SI es capicua")
else:
    print("La palabra ", s, " NO es capicua")
