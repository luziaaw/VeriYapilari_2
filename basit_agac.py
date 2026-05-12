class Kutu:
    def __init__(self, isim):
        self.isim = isim       # Klasörün adı
        self.icindekiler = []  # İçindeki diğer klasörler veya dosyalar

# 1. Ana Klasörü (Root) oluşturalım
ana_klasor = Kutu("Ödevlerim")

# 2. Alt klasörleri oluşturalım
ders_1 = Kutu("Matematik")
ders_2 = Kutu("Python")

# 3. Bunları ana klasörün içine koyalım (İlişki kuruyoruz)
ana_klasor.icindekiler.append(ders_1)
ana_klasor.icindekiler.append(ders_2)

# 4. Python klasörünün içine bir dosya atalım
dosya = Kutu("odev.py")
ders_2.icindekiler.append(dosya)

# --- Hadi bakalım ne yaptık? ---
print(f"Ana dizin: {ana_klasor.isim}")
print(f"Içindeki klasörler: {ana_klasor.icindekiler[0].isim} ve {ana_klasor.icindekiler[1].isim}")
print(f"Python klasörünün içindeki dosya: {ders_2.icindekiler[0].isim}")
