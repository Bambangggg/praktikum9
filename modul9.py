def write_file():
    input_nama = input("masukkan nama: ")
    input_umur = input("masukkan umur: ")
    input_alamat = input("masukkan alamat: ")
    input_email = input("masukkan email: ")
    input_dosenwali = input("masukkan dosen wali: ")

    fileWrite = open("biodata.txt", "w")
    fileWrite.write("nama: " + input_nama + "\numur: " + input_umur + "\nalamat: " + input_alamat + "\nemail: " + input_email + "\ndosen wali: " + input_dosenwali)
    fileWrite.close()

def read_file():
    fileRead = open("biodata.txt", "r")
    text = fileRead.read()
    print("ini data anda:")
    print(text)
    fileRead.close()

write_file()
read_file()
