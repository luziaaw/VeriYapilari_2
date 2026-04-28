
class Dugum:
    def __init__(self, veri):
        self.data = veri  # Düğümün içindeki bilgi 📦
        self.next = None  # Bir sonraki kutuyu gösteren ok ➡️

# 1. Adım: Düğümleri tek tek oluşturalım
hucre1 = Dugum("Hücre A")
hucre2 = Dugum("Hücre B")
hucre3 = Dugum("Hücre C")

# 2. Adım: self.next özelliğini kullanarak düğümleri zincirleyelim
hucre1.next = hucre2  # A'dan B'ye yol yaptık
hucre2.next = hucre3  # B'den C'ye yol yaptık

# 3. Adım: Manuel olarak ekrana yazdıralım
print("Zincir Başlıyor! 👇")
print(f"1. Durak: {hucre1.data}")
print(f"2. Durak: {hucre1.next.data}") # hucre1'in sonrasındaki veriyi al
print(f"3. Durak: {hucre1.next.next.data}") # İki adım sonrasına git