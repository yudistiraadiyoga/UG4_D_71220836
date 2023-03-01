def kp(kalimat):
    kata = kalimat.split()
    panjang = ('')
    for kata in kata:
        if len(kata)>len(panjang):
            panjang=kata
    return panjang
    
kalimat = str(input('Masukkan sebuah kalimat\t: '))
print(f'Kata terpanjang dalam kalimat tersebut adalah {kp(kalimat)}')
