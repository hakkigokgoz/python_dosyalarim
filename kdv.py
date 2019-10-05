# -*- coding: utf-8 -*-
# Kdv sini almak istediğiniz sayıyı girin değişkende tut 

sayi=float(input('Kdv''sini almak istediğiniz tutar giriniz : '))
#sayii değişkenini 0.18 ile çarp ve kdv değişkenine ata

kdv=0.18*sayi
print('Tutar:' , sayi)
print('Kdv : ' , kdv)
print('Kdv dahil tutar:', sayi+kdv)

