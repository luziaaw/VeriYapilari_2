
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None # Listenin en başı

    # Listenin sonuna yeni düğüm ekleme
    def ekle(self, yeni_veri):
        yeni_dugum = Node(yeni_veri)
        if self.head is None:
            self.head = yeni_dugum
            return
        
        son_dugum = self.head
        while son_dugum.next:
            son_dugum = son_dugum.next
        son_dugum.next = yeni_dugum

    # Listeyi ekrana yazdırma
    def listele(self):
        temp = self.head
        while temp:
            print(f"[{temp.data}]", end=" -> ")
            temp = temp.next
        print("Bitti! ✅")

# Uygulama
liste = LinkedList()
liste.ekle("Python")
liste.ekle("Java")
liste.ekle("C++")
liste.listele()