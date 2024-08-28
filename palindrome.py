def palindrom(s):
    return s == s[::-1]


s = input()
ans = palindrom(s)

if ans:
    print("Ja, meningen är en palindrom")
else:
    print("Nej, meningen är inte en palindrom")