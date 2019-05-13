# BAHASA INDONESIA VERSION

# program sederhana untuk keputusan menabung dari upah/gaji

# membuat kelas border/garis tepi berupa judul dan pembatas form program
class BORDER_:
    def title():
        print (("="*27)+" KEPUTUSAN MENABUNG DARI GAJI/UPAH BULANAN "+("="*27))

    def print2strip():
        print (("="*100))

    def print_strip():
        print (("-"*100))
        
    def print_end():
        print (("="*30)+("<>"*20)+("="*30))

# =============================================================================

# inti program
BORDER_.title()
while True:
    try:
        income = int(input("Masukkan Upah/Gaji Anda : . . .Rp"))
        break
    except:
        print("\nInput ditolak. Silahkan coba lagi!\n")
BORDER_.print2strip()

# format awal untuk data biaya dan item kebutuhan harian/bulanan
day_cost = 0
month_cost = 0
item = []
lst_d_m = []
cst = []
# ...termasuk untuk legenda kebutuhan
pilihan_hb={'H' : 'Kebutuhan Harian', 'B' : 'Kebutuhan Bulanan'}

while True:    
    # form kebutuhan
    name_ = str(input("Nama kebutuhan Anda :  . . "))
    day_month = str(input("\nKebutuhan Harian/Bulanan? (H/B)  . . "))
    item.append(name_)
    lst_d_m.append(pilihan_hb[day_month])
    
    # memasukkan input biaya (harian/bulanan)
    if day_month == 'H':
        costd = int(input("\nBiaya kebutuhan {} : . . Rp".format(name_)))
        day_cost += costd
        cst.append(str(costd))
    
    elif day_month == 'B':
        costm = int(input("\nBiaya kebutuhan {} : . . Rp".format(name_)))
        month_cost += costm
        cst.append(str(costm))
        
    #konfirmasi penambahan kebutuhan
    confirm_ = input('\nApakah masih ada kebutuhan lain? (Y/T) . . ')
    BORDER_.print_strip()
    if confirm_ == 'Y':
        continue
    elif confirm_ == 'T':
        break

# patokan hari kerja dalam 1 bulan
days = int(input("Waktu hari kerja dalam 1 bulan : ... "))

# rumus perhitungan (termasuk zakat jika sesuai kaidah)
zakat = income * float(2.5/100)
netto = income - (((day_cost) * days) + (month_cost))

# inout tabungan/investasi
invest = int(input("\nJumlah uang yang akan Anda tabung : .. Rp"))

# hasil keputusan
BORDER_.print2strip()
if netto >= invest:
    print ("Sisa gaji/upah Anda sebesar Rp{}. Sudah cukup untuk menabung Rp{} .\nBila sesuai kaidah, bayarlah  Rp{} untuk Zakat Profesi!".format(netto, invest, zakat))
elif invest >= netto >= 0:
    print ("Anda tidak bisa menabung sebesar Rp{} dengan sisa gaji/upah Rp{} !\nSegera berhemat dan atur kembali kebutuhan Anda :( !!!".format(invest, netto))
else:
    print ("ANDA DARURAT HUTANG Rp{} ! MOHON SEGERA MELUANSINYA ! ! !".format((-1)*netto))


# penyusunan format daftar dari dict
daftar = dict(zip(zip(item, lst_d_m), cst))

print("\nDaftar Kebutuhan Anda:\n"+('---'*33))
for tanda in daftar:
    print(tanda[0],'\t\t--  ',tanda[1],'\t--->\tRp',daftar[tanda])

BORDER_.print_end()
