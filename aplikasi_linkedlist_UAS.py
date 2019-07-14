import os
 
# Membuat class untuk node
class Node(object):
 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
   
    # Mengambil data dari node
    def get_data(self):
        return self.data
   
    # Mengambil node berikutnya
    def get_next(self):
        return self.next_node
   
    # Menentukan node berikutnya
    def set_next(self, new_next):
        self.next_node = new_next
       
# Membuat class untuk linked list
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
   
    # Menambah node baru
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
 
    # Menghitung panjang list
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
 
    # Mencari sebuah data pada list
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
               
        return found
 
    # Menghapus node
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
 
    # Menampilkan isi dari list
    def showData(self):
        os.system('clear')
        print ("Tampilkan list data:")
        print ("Node -> Next Node")
        current_node = self.head
        while current_node is not None:
            print (current_node.data),
            print ("   ->")
           
            current_node = current_node.next_node
 
    # Main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("clear")
            print("===============================")
            print("|  Aplikasi Pendataan Buku    |")
            print("===============================")
            print("|1. Insert data               |")
            print("|2. Delete data               |")
            print("|3. Cari data                 |")
            print("|4. Panjang dari linked list  |")
            print("|5. Tampil data               |")
            print("===============================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="1"):
                os.system("clear")
                obj = str(input("Masukan Buku yang ingin anda tambahkan: "))
                self.insert(obj)
            elif(pilihan=="2"):
                os.system("clear")
                obj = str(input("Menghapus Buku... : "))
                self.delete(obj)
                x = input("")
            elif(pilihan=="3"):
                os.system("clear")
                obj = str(input("Buku yang ingin dicari: "))
                status = self.search(obj)
                if status == True:
                    print("Data ada kok :"+"\n"+ obj)
 
                else:                  
                    print("Data tidak ditemukan")
                x = input("")
            elif(pilihan=="4"):
                os.system("clear")
                print("Panjang dari queue adalah: "+str(self.size()))
                x = input("")
            elif(pilihan=="5"):
                os.system("clear")
                self.showData()
                x = input("")
            else:
                pilih="n"
 
if __name__ == "__main__":
    l = LinkedList()
    l.mainmenu()
