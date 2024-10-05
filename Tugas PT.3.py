# Tentukan gaji karyawan per jam berdasarkan golongan
upah_per_jam = {
    'A': 5000,
    'B': 7000,
    'C': 8000,
    'D': 10000
}

def hitung_gaji(nama, golongan, jam_kerja):

    if golongan not in upah_per_jam:
        return f"Golongan tidak valid untuk {nama}"

    upah_jam = upah_per_jam[golongan]

    gaji_pokok = upah_jam * jam_kerja

    if jam_kerja > 48:
        uang_lembur = (jam_kerja - 48) * 4000
    else:
        uang_lembur = 0

    total_gaji = gaji_pokok + uang_lembur
    
    return f"Nama Karyawan: {nama}, Total Gaji: {total_gaji}"

nama = input("Masukkan nama karyawan: ")
golongan = input("Masukkan golongan karyawan (A/B/C/D): ").upper()
jam_kerja = int(input("Masukkan jam kerja: "))

print(hitung_gaji(nama, golongan, jam_kerja))
