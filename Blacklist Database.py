# menggunakan tabulate untuk visualisasi tabel di terminal 
from tabulate import tabulate

# dummy data input manual didalam dictionary
blacklist_database =    {
                        'user_id': [1, 2, 3, 4, 5],
                        'name': ['Agus', 'Budi', 'Citra', 'Dina', 'Eko'],
                        'phone': [6281234567891, 6281234567892, 6281234567893, 6281234567894, 6281234567895],
                        'reason': ['Rule 1', 'Rule 2', 'Rule 3', 'Rule 4', 'Rule 5'],
                        "is_blocked": [True, True, True, False, False]
                        }

# Function menampilkan blacklist database
def show_database() :
    data = list(zip(*blacklist_database.values())) # merubah dari dictionary ke dalam list untuk mendukung function tabulate
    print(tabulate(data, headers = blacklist_database.keys(), tablefmt="grid")) # menampilkan database dalam bentuk tabel

# Main Program
while True:
    print('''=== Sistem Manajemen Blacklist Database ===

    1. Menampilkan Database
    2. Menambahkan Data Akun
    3. Mengupdate Data Akun
    4. Menghapus Data Akun
    5. Mencari Akun
    6. Keluar Program''')
    
    try:
        input_menu = int(input('Masukkan angka menu (1-6): ')) # memilih menu di sistem
    except ValueError:
        print('Masukkan angka yang valid')
        continue # akan kembali ke program awal loop

    if input_menu == 6: # keluar program
        print('Keluar dari sistem. Tetap waspada terhadap aktivitas mencurigakan!!!')
        break 

    if input_menu == 5: # mencari akun di database
        while True:
            print('== Mencari akun di blacklist database, based on user id ===')

            try:
                cari_user_id = int(input('Masukkan user id: '))
            except ValueError:
                print('Masukkan user id yang valid')
                continue # akan kembali ke program awal loop

            if cari_user_id in blacklist_database['user_id']: 
                
                hasil_index = blacklist_database['user_id'].index(cari_user_id) # mencari index dari user id yang diinput

                # menampilkan data berdasarkan nama key & index dari user id yang di input
                print(f'''=== Akun Ditemukan ===
                User ID: {blacklist_database['user_id'][hasil_index]}
                Nama: {blacklist_database['name'][hasil_index]}
                Phone: {blacklist_database['phone'][hasil_index]}
                Reason: {blacklist_database['reason'][hasil_index]}
                Is Blocked: {blacklist_database['is_blocked'][hasil_index]}''')

                print(' Ingin mencari user yang lain (y/n):')
                cari_user_lagi = input('masukkan pilihan y untuk yes, n untuk no: ')
                if cari_user_lagi == 'y':
                    continue
                else:
                    print('=== Terima kasih ===')
                    break

            else:
                print('User id tidak ditemukan, mau cari yang lain (y/n):')
                cari_lain = input('masukkan pilihan y untuk yes, n untuk no: ')
                if cari_lain == 'y':
                    continue
                else:
                    print('=== Terima kasih ===')
                    break
    
    if input_menu == 1: # menampilkan database
        while True:
            print('=== Database Blacklist ===')
            show_database() # memanggil function def show_database
            print('=== Terima kasih ===')
            break

    if input_menu == 2: # menambahkan akun
        while True:
            try:
                user_id = int(input('Masukkan User ID baru:'))

                if user_id in blacklist_database['user_id']: # memastikan user id adalah unique 
                    print('User ID sudah ada di database')
                    continue
            except ValueError:
                print('User ID harus berupa angka')
                continue
            
            name = input('Masukkan Nama:')
            phone = int(input('Masukkan Nomor Telepon (diawali 62): '))
            reason = input('Masukkan reason (Format --> Rule x): ')

            while True:
                is_blocked = input('Apakah akun diblokir (y/n): ') 
                if is_blocked == 'y':
                    is_blocked = True
                    break
                elif is_blocked == 'n':
                    is_blocked = False
                    break
                else:
                    print("Input status blokir tidak valid, gunakan 'y' atau 'n'.")
                    continue
            
            blacklist_database['user_id'].append(user_id)
            blacklist_database['name'].append(name)
            blacklist_database['phone'].append(phone)
            blacklist_database['reason'].append(reason)
            blacklist_database['is_blocked'].append(is_blocked)

            print('=== Akun berhasil ditambahkan ke database ===')
            print('=== Database Blacklist ===')
            show_database() # memanggil function def show_database

            print('Ingin menambahkan user ID yang lain? (y/n):')
            nambah_lain = input('masukkan pilihan y untuk yes, n untuk no: ')
            if nambah_lain == 'y':
                continue
            else:
                print('=== Terima kasih ===')
                break
    
    if input_menu == 3: # update data akun
        while True:
            try:
                user_id = int(input('Masukkan User ID yang ingin diubah:'))

                if user_id not in blacklist_database['user_id']:
                    print('User ID tidak ditemukan di database')
                    continue
            except ValueError:
                print('User ID harus berupa angka')
                continue

            index_user = blacklist_database['user_id'].index(user_id) # mencari nomor index dari user ID input

            while True:
                print('''=== Pilih data yang ingin di ubah ===
                1. Nama
                2. Nomor Telepon
                3. Reason
                4. Status Blokir akun''')

                ubah_data = int(input('Masukkan pilihan (1-4): '))

                if ubah_data == 1: # mengubah nama
                    nama_baru = input('Masukkan nama baru: ')
                    blacklist_database['name'][index_user] = nama_baru
                
                    print('=== Data akun di database berhasil diubah ===')
                    print('=== Database Blacklist ===')
                    show_database() # memanggil function def show_database
                    break

                if ubah_data == 2: # mengubah nomor
                    while True:
                        try:
                            nomor_baru = int(input('Masukkan Nomor Telepon (diawali 62): '))
                        except ValueError:
                            print("Nomor telepon harus berupa angka.")
                            continue
                        break
                    
                    blacklist_database['phone'][index_user] = nomor_baru
                
                    print('=== Data akun di database berhasil diubah ===')
                    print('=== Database Blacklist ===')
                    show_database() # memanggil function def show_database
                    break

                if ubah_data == 3: # mengubah reason blokir
                    reason_baru = input('Masukkan reason baru (format --> Rule x): ')
                    blacklist_database['reason'][index_user] = reason_baru
                
                    print('=== Data akun di database berhasil diubah ===')
                    print('=== Database Blacklist ===')
                    show_database() # memanggil function def show_database
                    break

                if ubah_data == 4: # mengubah status blokir
                    while True:
                        new_blocked_status = input('Status blokir akun terbaru (y/n): ') 
                        if new_blocked_status == 'y':
                            new_blocked_status = True
                            blacklist_database['is_blocked'][index_user] = new_blocked_status
                            break
                        elif new_blocked_status == 'n':
                            new_blocked_status = False
                            blacklist_database['is_blocked'][index_user] = new_blocked_status
                            break
                        else:
                            print("Input status blokir tidak valid, gunakan 'y' atau 'n'.")
                            continue
                    
                    print('=== Data akun di database berhasil diubah ===')
                    print('=== Database Blacklist ===')
                    show_database() # memanggil function def show_database
                    break


                else:
                    print('Pilihan data tidak ada, masukkan angka 1-4')
                    continue
                
            print('Ingin mengubah data user ID yang lain? (y/n):')
            nambah_lain = input('masukkan pilihan y untuk yes, n untuk no: ')
            if nambah_lain == 'y':
                continue
            else:
                print('=== Terima kasih ===')
                break

    if input_menu == 4: # menghapus data
        while True:
            try:
                user_id = int(input('Masukkan User ID yang ingin dihapus:'))

                if user_id not in blacklist_database['user_id']:
                    print('User ID tidak ditemukan di database')
                    continue
            except ValueError:
                print('User ID harus berupa angka')
                continue

            index_user = blacklist_database['user_id'].index(user_id) # mencari nomor index dari user ID input

            for i in blacklist_database:
                blacklist_database[i].pop(index_user)
            
            print('=== Data akun di database berhasil dihapus ===')
            print('=== Database Blacklist ===')
            show_database() # memanggil function def show_database

            print('Ingin menghapus data user ID yang lain? (y/n):')
            nambah_lain = input('masukkan pilihan y untuk yes, n untuk no: ')
            if nambah_lain == 'y':
                continue
            else:
                print('=== Terima kasih ===')
                break

    print('Ingin memilih menu yang lain? (y/n):')
    menu_lagi = input('masukkan pilihan y untuk yes, n untuk no: ')
    if menu_lagi == 'y':
        continue
    else:
        print('Keluar dari sistem. Tetap waspada terhadap aktivitas mencurigakan!!!')
        break  

