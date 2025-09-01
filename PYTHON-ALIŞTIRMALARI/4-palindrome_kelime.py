#düz ve tersten yazılan kelimelerin doğruluğu

import string

# Kullanıcıdan metin al
metin = input("Bir kelime veya cümle girin: ")

# Küçük harfe çevir, boşlukları ve noktalama işaretlerini kaldır
temiz_metin = "".join(
    harf.lower() for harf in metin if harf.isalnum()
)

# Tersini al
ters_metin = temiz_metin[::-1]

# Kontrol et
if temiz_metin == ters_metin:
    print(f"'{metin}' bir palindromdur.")
else:
    print(f"'{metin}' bir palindrom değildir.")