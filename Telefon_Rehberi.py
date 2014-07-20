def kayitEkle() :

	dosya = open("rehber.txt","a")

	m = raw_input("Kullanici adini giriniz: ")
	h = raw_input("Kullanicinin telefon numarasini giriniz: ")

	satir = m + "\t"+ h+ "\n"

	dosya.write(satir)
	dosya.close()
	
def kisiArama() :

        dosya = open("rehber.txt","r")

        aranan = raw_input("Aramak istediginiz kisinin ismini giriniz: ")

        ara = dosya.readlines()

        for i in range(len(ara)) :

                sonraki = ara[i]
                bulunan = sonraki.find(aranan)

                if bulunan != -1 :
                        print ara[i]
                        break
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
print "3.Rehberden Kayit Silme"
print "4.Kayit Listesi"
print "5.Rehber Silme"

secim = input("Seciminizi giriniz: ")

if secim == 1 :
	kayitEkle()

elif secim == 2 :
	kisiArama()

elif secim == 3 :
	kayitListeleme()
	silme()

elif secim == 4 :
	kayitListeleme()

elif secim == 5 :
	rehberiSilme()
