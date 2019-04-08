#program sederhana untuk keputusan menabung dari upah/gaji

# membuat kelas border/garis tepi berupa judul dan pembatas form program
class BORDER_():
    def title():
        print (("="*32)+" KEPUTUSAN MENABUNG DARI GAJI/UPAH "+("="*32))

    def print2strip():
        print (("="*100))

    def print_strip():
        print (("-"*100))
        
    def print_end():
        print (("="*30)+("<>"*20)+("="*30))
        

# ======================================================================================================

# inti
BORDER_.title()
while True:
    try:
        income = int(input("Masukkan Upah/Gaji Anda : . . .Rp"))
        break
    except:
        print("Input ditolak. Silahkan coba lagi!")

BORDER_.print2strip()

# format awal untuk data biata dan item kebutuhan harian/bulanan
day_cost = 0
month_cost = 0
item = []
#lst = []
cst = []

if income == 0:
    print("\t\t\t\t\t\tSELESAI!")
    quit()

for form in range(0,income) :
    
    # form kebutuhan
    name_ = str(input("Nama kebutuhan Anda :  . . "))
    day_month = str(input("\nKebutuhan Harian/Bulanan? (H/B)  . . "))
    
    item.append(name_)
    #lst.append(day_month)
    
    
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
days = int(input("Banyaknya hari kerja dalam 1 bulan : ... "))

# rumus perhitungan (termasuk zakat jika sesuai kaidah)
zakat = income * float(2.5/100)
cost_total_days = (day_cost) * days
cost_total_months = (month_cost)
netto = income - cost_total_days - cost_total_months

# inout tabungan/investasi
invest = int(input("\nJumlah uang yang akan Anda tabung : .. Rp"))

# hasil keputusan
BORDER_.print2strip()
if netto >= invest:
    print ("Sisa gaji/upah Anda sebesar Rp{} cukup untuk menabung Rp{} .\nBila sesuai kaidah, bayarlah  Rp{} untuk Zakat Profesi!".format(netto, invest, zakat))
else:
    print ("Anda tidak bisa menabung sebesar Rp{} dengan sisa gaji/upah Rp{} !\nSegera berhemat dan atur kembali kebutuhan Anda :( !!!".format(invest, netto))
    
print("\nDaftar Kebutuhan Anda:", dict(zip(item , cst)))

BORDER_.print_end()
