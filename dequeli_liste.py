
from collections import deque

# 1. Boş bir liste (deque) açalım
# Bunu iki ucu açık bir boru gibi düşünebilirsin.
kuyruk = deque()

# 2. Kuyruğun sonuna birilerini ekleyelim (Sıradan bir sıra gibi)
kuyruk.append("Ali")
kuyruk.append("Ayse")
print(f"Sirada kimler var? -> {list(kuyruk)}")

# 3. Hop! Biri aradan kaynak yaptı ve en basa gecti (appendleft)
kuyruk.appendleft("Veli") 
print(f"Veli en basa kaynak yapti! -> {list(kuyruk)}")

# 4. En bastaki islemini bitirdi ve gitti (popleft)
giden = kuyruk.popleft()
print(f"{giden} siradan ayrildi. Kalanlar: {list(kuyruk)}")

# 5. En sondaki de vazgecti, o da gitti (pop)
vazgecen = kuyruk.pop()
print(f"{vazgecen} beklemekten sıkıldı ve gitti. Son durum: {list(kuyruk)}")

# 6. Bakalım içeride kaç kişi kaldı?
print(f"Su an sirada {len(kuyruk)} kisi var.")
