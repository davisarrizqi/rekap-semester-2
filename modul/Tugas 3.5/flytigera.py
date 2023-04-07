import os
import random
import re
import time

"""
    PENUGASAN 3.5 - OLEH DAVIS ARRIZQI,
    TUGAS --> Modifikasi sehingga sesuai 
    dengan aturan suit di Indonesia
"""

def check_play_status():
    valid_responses = ['ya', 'tidak']
    while True:
        try:
            response = input('Apakah anda akan bermain lagi? (Ya atau Tidak): ')
            if response.lower() not in valid_responses:
                raise ValueError("Aturan Jawaban: Ya atau Tidak")

            if response.lower() == 'ya':
                return True
            else:
                os.system('cls' if os.name=='nt' else 'clear')
                print('Terimakasih karena sudah bermain!')
                exit()

        except ValueError as err:
            print(err)


def play_rps():
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Batu, Gunting, Kertas - Gass!')

        user_choice = input('Silahkan ambil pilihan anda: '
                            '[B]atu, [G]unting, atau [K]ertas: ')

        if not re.match("[BbGgKk]", user_choice):
            print('Silahkan pilih diantara berikut ini: ')
            print('[B]atu, [G]unting, atau [K]ertas:')
            continue

        print(f'Pilihan anda: {user_choice}')

        choices = ['B', 'G', 'K']
        opp_choice = random.choice(choices)

        print(f'Saya memilih: {opp_choice}')

        if opp_choice == user_choice.upper():
            print('Ups sepertinya seri!')
            play = check_play_status()

        elif opp_choice == 'B' and user_choice.upper() == 'G':
            print('Batu mengalahkan Gunting, Saya menang!')
            play = check_play_status()

        elif opp_choice == 'G' and user_choice.upper() == 'K':
            print('Gunting mengalahkan Kertas, Saya menang!')
            play = check_play_status()

        elif opp_choice == 'K' and user_choice.upper() == 'B':
            print('Kertas mengalahkan Batu, Saya menang!')
            play = check_play_status()

        else:
            # membuat logic tambahan
            listPilihan = { 'B' : 'Batu', 'G' : 'Gunting', 'K' : 'Kertas'} 
            print(f'Anda Menang!, {listPilihan[user_choice]} mengalahkan {listPilihan[opp_choice]}\n')
            play = check_play_status()


if __name__ == '__main__':
    play_rps()