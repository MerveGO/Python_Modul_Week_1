#SORU-1
print(*range(0,10))


#SORU-2
#for dongusu ile
veri=int(input("Lutfen bir sayi giriniz:"))
for x in range(0,veri):
    if x %2==0:
      print(x)

#while dongusu ile
sayi=int(input("Lutfen bir sayi giriniz:"))
i=0
while i<sayi:
 if i %2==0:
  print(i)
 i +=1


#SORU-3
ilk=int(input("Baslangic sayisi giriniz:"))
son=int(input("Bitis sayisi giriniz:"))
for x in range(ilk,son+1):
    print(x)

#SORU-4
sayi=int(input("Bir sayi giriniz:"))
if sayi%2==0:
  print (f"Girdiginiz {sayi} sayisi cifttir.")
else:
  print(f"Girdiginiz {sayi} sayisi tektir.")

#SORU-5
sayi=int(input("Faktoriyeli hesaplanacak pozitif bir sayi giriniz:"))
faktoriyel=1
for i in range(1,sayi+1):
    faktoriyel *=i
print(f"{sayi} ! =",faktoriyel)

#SORU-6
sayi=int(input("Asalligi bulunacak bir sayi giriniz:"))
bolen_sayisi=0
for i in range(2,sayi+1):
    if sayi%i == 0 :
        bolen_sayisi+=1
if bolen_sayisi==1:        
    print(f"{sayi} sayisi asaldir.")
else:
    print(f"{sayi} sayisi asal degildir.")

#SORU-7
#Soruyu iki farkli sekilde anladigim icin iki cozum giriyorum.
#cozum1
adet=int(input("Kac adet fibonacci sayisi girilsin:"))
a1=0
a2=1
liste=[]
liste.append(a1)
liste.append(a2)
for i in range(adet-2):
   a3 = a1+a2 
   a1,a2 = a2,a3
   liste.append(a3)
print("fibonacci listesi:",liste) 

#cozum2
limit=int(input("Hangi sayiya kadar fibonacci dizisi girilsin:"))
fibonacci_liste=[]
a=0
b=1
while a<limit:
   fibonacci_liste.append(a)
   a,b = b,a+b
print("fibonacci listesi:",fibonacci_liste )  

#SORU-8
kelime=input("Bir kelime girniz:")
print("Ters kelime:",kelime[::-1])

#SORU-9
while True:
 veri=input("Bir kelime giriniz(cikmak icin q'ya basiniz.):")
 if veri=="q":
   print("program sonlandiriliyor..")
   break
 elif veri==veri[::-1]:
    print(f"Girdiginiz {veri} kelimesi palindromdur.")
 else:
   print(f"Girdiginiz {veri} kelimesi palindrom degildir.") 

#SORU-10
kilo=float(input("Kilonuz (kg cinsinden):"))
boy=float(input("Boyunuz (metre cinsinden(orn:1.65):"))
     #BMI(BOY\KILO ENDEKSI)=kilo/(boy**2)
BMI=kilo/(boy**2)
print("Kilo endeksiniz:",BMI)
if BMI<25:
    print("Zayifsiniz..")
elif 25<=BMI<30:
    print("Ideal kilonuzdasiniz..")
elif 30<=BMI<40:
    print("Kilolusunuz..")
else :
    print("Fazla kilolusunuz..")

#SORU-11
print("3 adet sayi giriniz..")
liste=[]
for x in range(1,4):
    sayi=int(input(f"{x}. sayi:"))
    liste.append(sayi)
print("En buyuk sayi:",max(liste))

#SORU-12
for x in range(1,5):
    ara_sinav=float(input(f"Ders{x} icin ara sinav notu giriniz:"))
    final=float(input(f"Ders{x} icin final notu giriniz:"))
    ortalama=(ara_sinav * 0.4 )+ (final * 0.6)

    if ortalama >= 50:
      print(f"Ders{x} icin ortalamaniz:{ortalama}\nBASARILI")
    else:
      print(f"Ders{x}icin Ortalamaniz:{ortalama}\nBASARISIZ")



  
