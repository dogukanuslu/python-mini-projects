def mini_atm():
    doğru_kullanici = "Admin"
    doğru_şifre = "1234"
    bakiye = 1000
    while True:
        kullanici_adiniz = input("Kullanici adinizi girin: ")
        şifre = input("Şifrenizi girin: ")

        if kullanici_adiniz == doğru_kullanici and şifre == doğru_şifre:
            print("Giriş İşlemi Başarilidir. Hoşgeldiniz.\n")
            break
        else:
            print("Hatali kullainici adi veya şifre! Tekrar Deneyiniz.\n")
    

    while True:
        print("\n.=== Mini ATM uygulamasi===")
        print("1. Bakiye Görüntüle")
        print("2. Para Yatir")
        print("3. Para Çek")
        print("4. Çikiş")        

        seçim = input("Lütfen 1-4 arasindan seçiminizi yapiniz:")

        if seçim == "1":
            print(f"Mevcut Bakiyeniz: {bakiye} TL")

        elif seçim == "2":
            miktar = float(input("Yatirmak istediğiniz miktari giriniz:"))
            if miktar > 0:
                bakiye += miktar
                print(f"{miktar} TL Yatirildi. Güncel Bakiyeniz:{bakiye} TL")
            else:
                print("Lütfen Geçerli Bir Miktar Giriniz. ")

        elif seçim == "3":
            miktar = float(input("Çekmek İstediğiniz Miktari Giriniz: "))
            if miktar > 0:
                if miktar <= bakiye:
                    bakiye -= miktar
                    print(f"{miktar} TL Çekildi. Güncel Bakiyeniz: {bakiye} TL ")   
                else:
                    print("Yetersiz Bakiye")
            else:
                print("Lütfen Geçerli Bir Miktar Giriniz. ")

        elif seçim == "4":
            print("Çikiş Yapiliyor, Hoşça kalin ")      
        else:
            print("Geçersiz Seçim! Lütfen 1-4 Arasinda Bir Değer Giriniz. ")
