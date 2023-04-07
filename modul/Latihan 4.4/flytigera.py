# logic by davis arrizqi
import os; import random
listBarang = []; os.system("cls")

def tambahBarang():
    global listBarang   # mengambil value dari global value
    namaBarang = input("\n    Masukkan Nama Barang: ")
    listBarang.append(namaBarang)
    print("    Berhasil Menginput Barang!\n")
    # masih bisa dikembangkan dengan fitur konfirmasi input

def lihatBarang(listBarangTersedia=listBarang):
    print("    Data Tersedia: ")
    for data in range(len(listBarangTersedia)):
        print(f'    {data+1}). {listBarangTersedia[data]}')

def hapusBarang(listBarangTersedia=listBarang):
    lihatBarang(listBarangTersedia); global listBarang; print('')
    barangDihapus = input("    Barang Yang Ingin Dihapus: ")

    # terus melakukan perulangan ketika barang masih belum tersedia
    while barangDihapus not in listBarang:
        print("\n    Barang Tidak Tersedia!"); print(listBarang)
        barangDihapus = input('    Barang Yang Ingin Dihapus: ')
    if(barangDihapus != 'skip'): print(f'    Berhasil menghapus {barangDihapus}!')

def fungsiEksekusi():
    menuDipilih = None; listSalamPerpisahan = ['Goodbye!', 'Farewell!', 'Bye!', 'See you later!', "¡Adiós!", "¡Hasta luego!", "¡Chao!", "¡Hasta la vista!"]
    while menuDipilih != '4':
        print(
        """
    ========  MENU KERANJANG ========
    1. Tambahkan Barang
    2. Lihat Keranjang
    3. Hapus Barang
    4. Keluar
    ================================= """
        ); menuDipilih = input("    Pilihan Anda: "); print('')

        # masih bisa dikembangkan dengan fitur searching index
        if(menuDipilih == '1'): tambahBarang()
        elif(menuDipilih == '2'): lihatBarang()
        elif(menuDipilih == '3'): hapusBarang()
        elif(menuDipilih == '4'): break
        else: print('Menu Tidak Tersedia! - Pilih Antara 1-4')

        os.system('pause'); os.system("cls")
    try: print('   ', listSalamPerpisahan[random.randrange(0, len(listSalamPerpisahan)-1)])
    except: print('    Selesai') # logika untuk membuat suatu salam akhir yang berbeda beda

if __name__ == '__main__':
    fungsiEksekusi()