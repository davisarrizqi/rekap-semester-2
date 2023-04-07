import random

namaPemain = {
    '1' : 'Manuel Neuer',
    '2' : 'Dayot Upamecano',
    '4' : 'Matthis de Ligt',
    '5' : 'Benjamin Pavard',
    '6' : 'Joshua Kimmich',
    '7' : 'Serge Gnabry',
    '8' : 'Leon Goretzka',
    '10' : 'Leroy Sané',
    '11' : 'Kingsley Coman',
    '13' : 'Eric M. Choupo-Moting',
    '14' : 'Paul Wanner',
    '17' : 'Sadio Mané',
    '19' : 'Alphonso Davies',
    '20' : 'Bouna Sarr',
    '21' : 'Lucas Hernandez',
    '22' : 'João Cancelo',
    '23' : 'Daley Blind',
    '25' : 'Thomas Müller',
    '26' : 'Sven Ulreich',
    '27' : 'Yann Sommer',
    '35' : 'Johannes Schenk',
    '38' : 'Ryan Gravenberch',
    '39' : 'Mathys Tel',
    '40' : 'Noussair Mazraoui',
    '42' : 'Jamal Musiala',
    '44' : 'Josip Stanišić'
}    # nama pemain bayern

def showPlayer(dictPemain=namaPemain):
    print('==== Nama Pemain Bayern: ====')
    for data in dictPemain:
        print(f'> Pemain {dictPemain[data]} [{data}]')
    print('=============================')

if __name__ == '__main__':
    showPlayer()