def aritmatika(a,d,n):
    s = n/2*(2*a+(n-1)*d)
    return s
print('='*20,' BARIS ARITMATIKA ','='*20)
a = float(input('Masukkan bilangan awal\t\t: '))
d = float(input('Masukkan selisih bilangan\t: '))
n = float(input('Masukkan banyaknya suku\t\t: '))
print('Total dari deret aritmatika tersebut adalah\t:', aritmatika(a,d,n))