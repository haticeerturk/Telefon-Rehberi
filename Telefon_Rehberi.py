def kayitEkle() :

	dosya = open("rehber.txt","a")

	m = raw_input("Kullanici adini giriniz: ")
	h = raw_input("Kullanicinin telefon numarasini giriniz: ")

	satir = m + "\t"+ h+ "\n"

	dosya.write(satir)
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
print "2.Rehberden Kayit Silme"
print "3.Kayit Listesi"
print "4.Rehber Silme"

secim = input("Seciminizi giriniz: ")

if secim == 1 :
	kayitEkle()

elif secim == 2 :
	kayitListeleme()
	silme()

elif secim == 3 :
	kayitListeleme()

elif secim == 4 :
	rehberiSilme()
