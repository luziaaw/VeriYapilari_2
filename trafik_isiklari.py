
class Isik:
    def __init__(self, renk):
        self.renk = renk
        self.sonraki_isik = None

# Işıkları tanımlayalım
kirmizi = Isik("KIRMIZI 🔴")
sari = Isik("SARI 🟡")
yesil = Isik("YEŞİL 🟢")

# Döngüyü kuralım: Kırmızı -> Sarı -> Yeşil -> (Tekrar Kırmızıya dönebilir)
kirmizi.sonraki_isik = sari
sari.sonraki_isik = yesil
yesil.sonraki_isik = kirmizi # İşte bu bir dairesel bağlantı oldu! 🔄

# Bir tur döndürelim
su_anki_isik = kirmizi
for _ in range(4):
    print(f"Şu an yanan: {su_anki_isik.renk}")
    su_anki_isik = su_anki_isik.sonraki_isik