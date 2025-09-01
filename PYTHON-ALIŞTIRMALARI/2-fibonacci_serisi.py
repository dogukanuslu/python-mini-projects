def fibonacci(n):
    fib_serisi = [0,1]

    for i in range(2,n):
        yeni_sayi = fib_serisi[i-1] + fib_serisi[i-2]
        fib_serisi.append(yeni_sayi)
    return fib_serisi

terim_sayisi = int(input("Kaç terimlik bir Fibonacci serisi istiyorsunuz? : "))

if terim_sayisi <=0:
    print("Lütfen pozitif bir değer giriniz.")
elif terim_sayisi ==1:
    print([0])
    with open("fibonacci_serisi.txt", "w",) as dosya:
        dosya.write("Fibonacci serisi (1 terim): [0]")
else:
    sonuç = fibonacci(terim_sayisi)
    metin = f"Fibonacci serisi ({terim_sayisi} terim): {sonuç}"
    print(metin)

    with open("fibonacci_serisi.txt", "w",) as dosya:
        dosya.write(metin)

    import time

    start_time = time.time()
    with open("fibonacci_serisi.txt","w") as dosya:
        dosya.write(metin)
    end_time = time.time()
    print(f"Dosya yazma süresi: {end_time - start_time} saniye sürdü.")
        

    # 20.578 e kadar hesaplama yapıyor.