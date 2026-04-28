
from collections import deque

# 1. Bağlı listemizi (deque) oluşturalım
# Deque, hem baştan hem sondan hızlı ekleme/çıkarma yapar.
bagli_liste = deque(["Elma", "Armut", "Muz"])

print(f"İlk Liste: {bagli_liste} ✨")

# 2. Sona eleman ekleme (Array gibi)
bagli_liste.append("Çilek")

# 3. BAŞA eleman ekleme (Linked List'in gücü burada!)
# Normal listelerde başa eklemek zordur ama burada çok hızlıdır.
bagli_liste.appendleft("Kivi") 🥝

print(f"Güncel Liste: {bagli_liste}")

# 4. Aradan eleman çıkarma
bagli_liste.remove("Armut")

print(f"Son Durum: {bagli_liste} ✅")
