import heapq

# 1. Boş bir liste oluşturalım. 
# Bu liste bizim 'Heap' (Yığın) yapımız olacak.
acil_servis = []

# 2. Hastaları (sayıları) sıraya ekleyelim.
# 'heappush' kullandığımızda Python en küçük sayıyı hep en başa koyar.
heapq.heappush(acil_servis, 30) # Hafif yaralı
heapq.heappush(acil_servis, 10) # ÇOK ACİL! 🚨
heapq.heappush(acil_servis, 20) # Orta derece

print(f"Acil servis sırasının tamamı: {acil_servis}")

# 3. En küçük elemanı (en öncelikli olanı) görelim ama silmeyelim.
en_oncelikli = acil_servis[0]
print(f"Şu an en başta bekleyen (Min-Heap): {en_oncelikli}")

# 4. En öncelikli hastayı muayeneye alalım (pop işlemi)
# 'heappop' her zaman en küçük sayıyı çıkarır.
muayene_edilen = heapq.heappop(acil_servis)
print(f"Muayeneye alınan hasta numarası: {muayene_edilen}")

# 5. Bakalım yeni en öncelikli kim oldu?
print(f"Yeni sıra: {acil_servis}")
print(f"Yeni en öncelikli: {acil_servis[0]}")
