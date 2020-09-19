s = "Our capacity for love increases with each person we cross paths with."
m = 5
n = 21
print(s)
print(len(s))
ans = ''
if len(s) % 2 == 0:
    ans = 'y'
else:
    ans = 'n'
print("even? " + ans)
print('first symbol: ' + s[0])
print('last symbol: ' + s[len(s) - 1])
if s[m] == s[n]:
    ans = 'y'
else:
    ans = 'n'
print('check if symbol ' + str(m) + ' equals symbol ' + str(n) + ': ' + ans)
print('first ' + str(m) + ' symbols: ' + s[:m])
print('last ' + str(n) + ' symbols: ' + s[len(s)-n:])
p = s[len(s)-2]
s1 = p + s + p
print(s1)
s1 = s[:m] + s[m]*2 + s[m:]
print(s1)
s1 = s[1:len(s)-1]
print(s1)
s1 = s[m:]
print(s1)
s1 = s[:m] + s[n:]
print(s1)
s1 = s[0:len(s):2]
print(s1)
s1 = ''
for i in range(0,len(s)):
    s1 += s[i]*2
print(s1)