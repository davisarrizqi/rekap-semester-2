import random
import os

class KalkulatorSederhana:
    # parameter diberikan default value agar lebih fleksibel
    def __init__(self, bilangan1=2023, bilangan2=2005):
        self.bilangan1 = bilangan1
        self.bilangan2 = bilangan2
        self.hasilPenjumlahan = 0
        self.hasilPangkat = 1
        # default value untuk hasil perhitungan

    def setBilangan1(self):
        print(f'\nBilangan Saat Ini: {self.bilangan1}')
        pivotNumber = input("Masukkan Bilangan 1: ")
        
        # memastikan bahwa yang diinput adalah angka
        try: 
            pivotNumber = float(pivotNumber)
            self.bilangan1 = pivotNumber

        except:
            print('\nSilahkan input dengan benar!')
            self.setBilangan1() # melakukan perulangan sampai valid

    def setBilangan2(self):
        print(f'\nBilangan Saat Ini: {self.bilangan2}')
        pivotNumber = input("Masukkan Bilangan 2: ")
        
        # memastikan bahwa yang diinput adalah angka
        try: 
            # memastikan integer karena akan dijadikan pangkat
            pivotNumber = int(pivotNumber)
            self.bilangan2 = pivotNumber

        except:
            print('\nSilahkan input dengan benar!')
            self.setBilangan2() # melakukan perulangan sampai valid

    def tambah(self):
        print("\n==== PENJUMLAHAN ====")
        self.hasilPenjumlahan = self.bilangan1 + self.bilangan2
        print(f'Hasil : {self.bilangan1} + {self.bilangan2} = {self.hasilPenjumlahan}')
        print("=====================")

    def pangkat(self):
        print("\n==== PERPANGKATAN ====")     
        # memastikan bahwa bilangan2 minimal bernilai 1
        if(self.bilangan2 <= 0): self.bilangan2 = 1

        # membuat perulangan untuk perpangkatan
        for power in range(self.bilangan2):
            self.hasilPangkat *= self.bilangan1

        # menampilkan hasilnya
        print(f'Hasil : {self.bilangan1}^{self.bilangan2} = {self.hasilPangkat}')
        print('======================')

    def main(self):
        print("===== KALKULATOR =====")
        self.setBilangan1()
        self.setBilangan2()
        self.tambah(); self.pangkat()
        print('\n======================')
os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    calc = KalkulatorSederhana(18, 12)
    calc.main()