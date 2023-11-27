def create_and_write_file():
    file_name = input("Masukkan Nama File: ")
    nama = input("Masukkan Namamu: ")
    nim = input("Masukkan NIM kamu: ")
    tahun_angkatan = input("Masukkan tahun angkatanmu: ")

    with open(file_name + ".txt", 'w') as file:
        file.write("Nama: {}\n".format(nama))
        file.write("NIM: {}\n".format(nim))
        file.write("Tahun Angkatan: {}\n".format(tahun_angkatan))

    print("File Berhasil Dibuat")


def read_file():
    file_name = input("Masukkan Nama File: ")

    try:
    
        with open(file_name + ".txt", 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File tidak ditemukan")



def add_text_to_file():
    file_name = input("Masukkan Nama File: ")
    nama_sahabat = input("Masukkan Nama Sahabatmu: ")
    catatan_tambahan = input("Masukkan Catatan Tambahan kamu: ")

    try:
        # Membuka file untuk menambahkan teks
        with open(file_name + ".txt", 'a') as file:
            file.write("Nama Sahabat: {}\n".format(nama_sahabat))
            file.write("Catatan Tambahan: {}\n".format(catatan_tambahan))
        print("Data Berhasil Ditambahkan ke File")
    except FileNotFoundError:
        print("File tidak ditemukan")




while True:
    print("\n===Program File Handling ===\n")
    print("1. Membuat dan Menulis File")
    print("2. Membaca File")
    print("3. Menambahkan Text Pada File")
    print("4. Keluar Dari Program")

    pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4): ")

    if pilihan == '1':
        create_and_write_file()
    elif pilihan == '2':
        read_file()
    elif pilihan == '3':
        add_text_to_file()
    elif pilihan == '4':
        print("Keluar dari Program")
        break
    else:
        print("Pilihan tidak valid. Masukkan angka 1, 2, 3, atau 4.")
