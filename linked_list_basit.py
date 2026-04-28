
class Node:
    def __init__(self, data):
        self.data = data  # Veri kısmı
        self.next = None  # Bir sonraki düğümü gösteren işaretçi

# Düğümleri oluşturalım
dugum1 = Node("Elma")
dugum2 = Node("Armut")
dugum3 = Node("Muz")

# Düğümleri birbirine bağlayalım (Zincir oluşturuyoruz)
dugum1.next = dugum2
dugum2.next = dugum3

# Head (Başlangıç) düğümünden başlayarak yazdıralım
temp = dugum1
while temp:
    print(f"Düğüm Verisi: {temp.data} -> ", end="")
    temp = temp.next
print("None (Liste Bitti) ✨")