#tersten de yazsak okunup okunmadığını kontrol etme

for i in range(1000,100000):
    s = str(i)
    t=s[::-1]
    if s == t:
        print(s)


