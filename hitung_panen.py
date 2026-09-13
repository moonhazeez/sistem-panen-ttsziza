def hitung_total(panen_kg, harga_per_kg):
    return panen_kg * harga_per_kg

total = hitung_total(100, 15000)
print(f'Total Hasil Panen: Rp {total}')

def hitung_diskon(total, persen_diskon):
    return total * (persen_diskon / 100)

diskon = hitung_diskon(total, 5)
print(f'Diskon (5%): Rp {diskon}')
print(f'Total Bayar: Rp {total - diskon}')
