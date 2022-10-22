okul = "Sancaktepe Teknoloji Anadolu İmamhatip Lisesi"
makale = "Türkiye’nin inovasyon kapasitesini arttırabilmesi için yüksek nitelikli Fen, Teknoloji, Mühendislik ve Matematik (FeTeMM) işgücüne ihtiyacı vardır. Yirmibirinci yüzyılın değişen şart ve problemleriyle birlikte takım çalışması ve disiplinlerarası yaklaşımları doğuran bu ihtiyaç, gençlerimizi ve özellikle kız öğrencilerimizi erken yaşlardan itibaren FeTeMM araştırmaları yapabilecek şekilde eğitecek öğrenme ortamlarının tasarımını ve bu tasarımları etkin şekilde kullanabilecek öğretmenlerin yetiştirilmesini gerektirir. Buna mukabil yapılan araştırmalar göstermektedir ki, öğretmenlerimiz mesleklerine etkin bir FeTeMM eğitimi verebilmek için gerekli bütünleşik öğretmenlik bilgisinden yoksun şekilde başlamaktadır. Bu makalenin amacı araştırmacıları FeTeMM eğitimi üzerine yürüttükleri çalışmalarının sonuçlarını TURJE’de yayımlamak konusunda cesaretlendirmektir."

# Tüm karakterleri büyük harf yap: upper()

print (okul.upper())

# Tüm karakterleri küçük harf yap: lower()

print (okul.lower())

# Her kelimenin ilk harfini büyük yap: title()

print (okul.title())

# Karater dizisinin ilk karakterlerini büyük ,diğer karakterlerini küçük harf yapalım: capitalize()

print (okul.capitalize())

# Belirli bir ifade kaç defa yer alır

print (okul.count("a"))

# Büyük harf küçük harf duyarlı

print (okul.lower().count("a"))

# Soldaki ve Sağdaki Boşluk karakterlerini temizleyelim: strip()

ad = input("adınız: ")
print(ad.strip() + "|")

# Soldaki ve Sağdaki Belirli karakterleri temizleyelim: strip("ifade")

urun_kodu = "HEP20221022HEP"

print(urun_kodu.strip("HEP"))

# Soldaki boşluk veya belirli ifadeyi temizleyelim: lstrip()

print(ad + "|") #adı boşlukla gönderelim
print(ad.lstrip() + "|")
print(urun_kodu.lstrip("HEP"))

# Sağdaki boşluk veya belirli ifadeyi temizleyelim: rstrip()


print(ad + "|")  #adı boşlukla gönderelim
print(ad.rstrip() + "|")
print(urun_kodu.rstrip("HEP"))

# Karakter dizisini bölelim

print(okul.split())
print(makale.split("."))

# Böldüğünüz ve listeye dönüşen ifadeleri birleştirelim: join()

kelimeler = okul.split()
print(kelimeler)
print("---".join(kelimeler))

# Ortalayıp çıktı verme

print("ahmet".center(20, "."))