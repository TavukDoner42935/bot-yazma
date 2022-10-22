# Boş bir liste Tanımlayalım: []

liste = []

print (liste)

print(type(liste))


okul = "Sancaktepe Teknoloji Anadolu İmamhatip Lisesi"

kelimeler = okul.split()

print(kelimeler)



# Belirli bir sıradaki kelimeleri yazdıralım

print(kelimeler[0])  # ilk kelime
print(kelimeler[1])
print(kelimeler[2])
print(kelimeler[3])
print(kelimeler[4])

# print(kelimeler[5]) # hata verdi

print(kelimeler[-1])  # son kelime
print(kelimeler[-2])
print(kelimeler[-3])
print(kelimeler[-4])
print(kelimeler[-5])

ad = "Ahmet enes ozturk"

print(ad[0])  #A

print(ad[6:17])  #enes ozturk

print(ad[6:17:2])  #ee zuk

print(ad[::-1])  #krutzo sene temhA

print(ad[-8:-12:-1])  #sene


# Listeler içerisinde farklı türden veriler olabilir

liste = [1, 12.3, "Python", True, [1, 2, 3]]

print(liste[-1][-1])  #3

print(liste[4][-1])  #3

print(liste[4][2])  #3

# 2 listeyi birleştirme

liste2 = [1, 2, 3]

liste3 = [4, 5, 6]

liste4 = liste2 + liste3

liste5 = liste3 + liste2

print(liste4)
print(liste5)

