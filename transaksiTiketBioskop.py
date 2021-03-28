## 1. Program penghitung jumlah pendapatan transaksi tiket film ##

#list film
list_film = {
    'spiderman' : 5000,
    'ironman' : 3000,
}


# Input nama film #
nama_film = (input('Judul film ("help" untuk melihat list film): ')).lower()

while (nama_film == "help"):
    for i in list_film:
        print(i,": Rp",list_film[i])
    nama_film = (input('Judul film ("help" untuk melihat list film): ')).lower()

# Input jumlah tiket terjual #
jumlah_tiket = int(input('Jumlah tiket yang terjual: ')) 

# Input tiket terjual pada kota tertentu #
kota = input('Tiket terjual di kota mana saja? ')+"."


#Definisi function transaksi_tiket
def transaksi_tiket(nama_film, jumlah_tiket, *kota):
    harga = list_film[nama_film]

    total_pendapatan = jumlah_tiket * harga

    return print("Film",nama_film,"terjual sebanyak",jumlah_tiket,"tiket dengan total pendapatan Rp",total_pendapatan,"di kota",kota)


# Pemanggilan function
transaksi_tiket(nama_film, jumlah_tiket, kota) #argumen "kota" bisa diganti ke multi argumen string nama kota seperti "malang", "padang", "surabaya"
transaksi_tiket("ironman",220, "surabaya","malang","palembang","padang")

