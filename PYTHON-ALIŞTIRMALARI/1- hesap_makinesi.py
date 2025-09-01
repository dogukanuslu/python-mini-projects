import os
def toplam(a,b):
    return a+b 
def cikar(a,b):
    return a-b
def çarp(a,b):
    return a*b
def bölme(a,b):
    return a/b
while True:
    os.system('cls')
    print("""
    *** HESAP MAKİNESİ ***

    1-TOPLAMA
    2-ÇIKARMA
    3-ÇARPMA
    4-BÖLME
                    
    """)
    sec=input("SEÇİMİNİZ:")
    say_a=input("1. sayi:")
    say_b=input("2. sayi")

    if (sec=="1") :
        print (toplam(int(say_a),int(say_b)))
    elif (sec=="2") :
        print (cikar(int(say_a),int(say_b)))
    elif (sec=="3") :
        print (çarp(int(say_a),int(say_b)))
    elif (sec=="4") :    
        print (bölme((int(say_a),int(say_b))))
    else: 
        print("GEÇERSİZ İŞLEM")
    input("Devam etmek için ENTER")
