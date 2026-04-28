
def basit_hash_fonksiyonu(anahtar, tablo_boyutu):
    # Metindeki mantık: Karakterlerin toplamının tablo boyutuna bölümünden kalan (mod)
    # Örn: "ab" -> a=1, b=2 toplam=3. 3 % 7 = 3. index
    karakter_toplami = sum(ord(karakter) for karakter in anahtar)
    return karakter_toplami % tablo_boyutu

# 7 elemanlı boş bir tablo (Hash Table) oluşturalım
tablo_boyutu = 7
hash_tablosu = [None] * tablo_boyutu

# Verilerimizi ekleyelim
veriler = ["ab", "cd", "efg"]

print("--- Hashing İşlemi Başlıyor ---")
for veri in veriler:
    indeks = basit_hash_fonksiyonu(veri, tablo_boyutu)
    hash_tablosu[indeks] = veri
    print(f"'{veri}' verisi hesaplanan {indeks}. indekse yerleştirildi. 📍")

print("\nFinal Hash Tablosu:", hash_tablosu)
