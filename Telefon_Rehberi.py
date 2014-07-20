def kayitEkle() :

	ayni_kisi = 0
	m = raw_input("Kullanici adini giriniz: ")
	h = raw_input("Kullanicinin telefon numarasini giriniz: ")

	dosya = open("rehber.txt","r")

	satir = m + "\t"+ h+ "\n"

	kayit = dosya.readlines()
	
	for i in range(len(kayit)) :
		
		siradaki = kayit[i]
		ayni = siradaki.find(m)
		
		if ayni != -1 :
			ayni_kisi = 1
			
	dosya.close()
	
	if ayni_kisi == 1 :
		print "Bu kisi zaten kayitli!"
		
	else :
		dosya = open("rehber.txt","a")
		dosya.write(satir)
		dosya.close()
	
def kisiArama() :

	kisi_yok = 0
        dosya = open("rehber.txt","r")

        aranan = raw_input("Aramak istediginiz kisinin ismini giriniz: ")

        ara = dosya.readlines()

        for i in range(len(ara)) :

                sonraki = ara[i]
                bulunan = sonraki.find(aranan)

                if bulunan != -1 :
                        print ara[i]
                 
                else :
                	kisi_yok = 1
        if kisi_yok == 1 :
        	print "Bu kisi kayitli degil!"
        	
        dosya.close()
        

def kayitDegisim() :

        dosya = open("rehber.txt","r")

        kisi = raw_input("Kayiti degistirilecek kisinin ismini giriniz: ")

        kisiler = dosya.readlines()

        dizi = []

        for i in range(len(kisiler)) :

                digerKisi = kisiler[i]
                degistirilecek = digerKisi.find(kisi)

                if degistirilecek == -1 :

                        dizi.append(digerKisi)

                else :
                        a = raw_input("Yeni kullanici adini giriniz: ")
                        b = raw_input("Kullanicinin numarasini giriniz: ")

                        yeni = a + "\t" + b + "\n"

                        dizi.append(yeni)
        dosya.close()

        #Dosya yaziliyor...
        dosya = open("rehber.txt","w")

        dosya.writelines(dizi)
        dosya.close()


def silme() :
	
	dosya = open("rehber.txt","r")
	
	isim = raw_input("Silmek istediginiz ismi giriniz: ")
	
	kayitlar = dosya.readlines()

	yenikayitlar = []
	
	for i in range(len(kayitlar)) :

		siradaki = kayitlar[i]
		sonuc = siradaki.find(isim)

		if sonuc == -1 :
			yenikayitlar.append(kayitlar[i])

	dosya.close()
	
	#Dosya yaziliyor...
	dosya = open("rehber.txt","w")
	
	dosya.writelines(yenikayitlar)
	dosya.close()
	print "Kayit Silindi"	

def kayitListeleme() :
	
	dosya = open("rehber.txt","r")

	isimler = dosya.readlines()
	
	print "ADI","\t","\t","TELEFON"
	print "--------","\t","--------"	
	for i in range(len(isimler)) :
		print i+1,"-",isimler[i]

	dosya.close()
	

def rehberiSilme() :

	import os
	
	os.remove("rehber.txt")


print "\t","\t","MENU"
print "1.Kayit Ekleme"
print "2.Kisi Arama"
print "3.Kayit Duzenle"
print "4.Rehberden Kayit Silme"
print "5.Kayit Listesi"
print "6.Rehber Silme"

secim = input("Seciminizi giriniz: ")

if secim == 1 :
	kayitEkle()

elif secim == 2 :
	kisiArama()

elif secim == 3 :
	kayitDegisim()

elif secim == 4 :
	kayitListeleme()
	silme()

elif secim == 5 :
	kayitListeleme()

elif secim == 6 :
	rehberiSilme()
