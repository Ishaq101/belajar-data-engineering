## 2. Program penghitung selisih dari dua tanggal ##

# jumlah hari pada setiap bulan #
jumlahHariPerBulan = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

# deklarasi input #
input1 = input('input 1:')
input2 = input('input 2:')

# deklarasi function penghitung selisih hari dari dua tanggal #
def selisihTanggal(input1, input2):

    # spliting input dan konversi menjadi bilangan integer
    tahun1, bulan1, tanggal1 = input1.split('-')
    tahun1, bulan1, tanggal1 = int(tahun1), int(bulan1), int(tanggal1)

    tahun2, bulan2, tanggal2 = input2.split('-')
    tahun2, bulan2, tanggal2 = int(tahun2), int(bulan2), int(tanggal2)

    bulan_ke_hari1 = 0

    tahun_ke_hari2 = 0
    bulan_ke_hari2 = 0

    total1 = 0
    total2 = 0

    # konversi selisih tahun serta konversi ke hari
    for n in range(tahun1,tahun2):
        if (n % 4 != 0):
            tahun_ke_hari2 += 365
        else:
            tahun_ke_hari2 += 366


    # conditional 1 : kedua tahun dari kedua tanggal merupakan tahun kabisat 
    if ((tahun2 & 4 == 0) and (tahun1 % 4 == 0)):
        copy_jumlahHariPerBulan = jumlahHariPerBulan.copy()
        copy_jumlahHariPerBulan[2] = 29

        for bulan_1 in range(bulan1-1):
            bulan_ke_hari1 += copy_jumlahHariPerBulan.get(bulan_1+1)

        for bulan_2 in range(bulan2-1):
            bulan_ke_hari2 += copy_jumlahHariPerBulan.get(bulan_2+1)
            
        total1 = bulan_ke_hari1 + tanggal1
        
        total2 = tahun_ke_hari2 + bulan_ke_hari2 + tanggal2
        
        selisih = total2 - total1
        return print("selisih tanggal (hari):", selisih)

    # conditional 2 : tahun dari tanggal pertama kabisat, tahun dari tanggal kedua bukan kabisat
    elif ((tahun1 % 4 == 0) and (tahun2 % 4 != 0)):
        copy_jumlahHariPerBulan = jumlahHariPerBulan.copy()
        copy_jumlahHariPerBulan[2] = 29

        for bulan_1 in range(bulan1-1):
            bulan_ke_hari1 += copy_jumlahHariPerBulan.get(bulan_1+1)

        for bulan_2 in range(bulan2-1):
            bulan_ke_hari2 += jumlahHariPerBulan.get(bulan_2+1)

        total1 = bulan_ke_hari1 + tanggal1
        
        total2 = tahun_ke_hari2 + bulan_ke_hari2 + tanggal2
        
        selisih = total2 - total1
        return print("selisih tanggal (hari):", selisih)

    # conditional 2 : tahun dari tanggal pertama bukan kabisat, tahun dari tanggal kedua kabisat
    elif ((tahun1 % 4 != 0) and (tahun2 % 4 == 0)):
        copy_jumlahHariPerBulan = jumlahHariPerBulan.copy()
        copy_jumlahHariPerBulan[2] = 29

        for bulan_1 in range(bulan1-1):
            bulan_ke_hari1 += jumlahHariPerBulan.get(bulan_1+1)

        for bulan_2 in range(bulan2-1):
            bulan_ke_hari2 += copy_jumlahHariPerBulan.get(bulan_2+1)

        total1 = bulan_ke_hari1 + tanggal1
        total2 = tahun_ke_hari2 + bulan_ke_hari2 + tanggal2
        selisih = total2 - total1
        return print("selisih tanggal (hari):", selisih)    


selisihTanggal(input1, input2)


# To check the code, we can campare it with this website #
## http://www.timeadate.eu/pages/id/calculator-days-id.html ##