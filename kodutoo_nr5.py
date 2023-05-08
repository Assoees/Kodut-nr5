# Asso eesmäe
# 08.05.23
# Iseseisev töö 1


# 1.1 Tervitus Koostada programm, mis väljastaks ekraanile teksti Tere, maailm! täpselt sellisel kujul - koma ja hüüumärgiga.

print("Tere, maailm!")

# 1.2. Aasta liblikas

#1. real luuakse muutuja nimega aasta ning antakse sellele väärtuseks 2020 (arvuna)
aasta = 2020
#2. real luuakse muutuja nimega liblikas ning antakse sellele väärtuseks "teelehe-mosaiikliblikas" (sõnena)
liblikas = "teelehe-mosaiikliblikas"
#3. real luuakse muutuja nimega lause_keskosa ning antakse sellele väärtuseks ". aasta liblikas on " (sõnena)
lause_keskosa = ". aasta liblikas on "
#4. real luuakse muutuja nimega lause, mille väärtuse saamiseks ühendatakse üheks sõnaks muutujad aasta, lause_keskosa ja liblikas (vajadusel tuleb kasutada funktsiooni, mis teisendab arvu sõneks);
lause = str(aasta) + lause_keskosa + liblikas 
#5. real väljastatakse muutuja lause väärtus ekraanile.
print(lause)

#1.3. Pilved
#Pilvede alumise pinna (aluse) kõrguse järgi liigitatakse pilvi ülemise, keskmise ja alumise kihi pilvedeks.
#Ülemiste pilvede alus on kõrgemal kui 6 km, keskmistel pilvedel on 2-6 km kõrgusel, alumistel pilvedel on madalamal kui 2 km. Koostada programm, mis

#1. küsib kasutajalt pilvede aluse kõrgust (kilomeetrites),
pilv = float(input("Mis on pilve aluse kõrgus kilomeetrites(eralda meetrid punktiga): "))
#2. väljastab ekraanile Need on ülemised pilved, kui sisestatu on üle 6.0 km ja Need on alumised pilved kui võrdne või väiksem kui 6.0
#IF/else kasutamine
if pilv > 6.0:
    print("Need on ülemised pilved")
else:
    print("Need ei ole ülemised pilved")
    
    
#1.4 Bussid    
#Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega. Eeldame, et reisijaid on vähemalt üks. Koostada programm, mis küsib transporditavate inimeste arvu ja
#ühe bussi kohtade arvu(just sellises järjekorras) ning väljastab ekraanile, mitu bussi on vaja ja mitu inimest on viimases bussis (eeldusel, et kõik eelnevad bussid on täis).
from math import *  
#1. Kui palju on reisijaid
a = int(input("Kui palju on reisijaid: "))
#2. Mitme kohaline bus
b = int(input("Mitme kohaline on buss: "))
#3. Mitu bussi vaja ja ümardamine ülespoole
bus = ceil(a / b)
#4. Kui palju on reisijaid bussis, jäägi arvutamine
inimesed = a % b
#5. Vastus reisijate arv ja kohtade arv
print("Reisijate arv: ",a)
print("Kohtade arv: ",b)
#6. Mitu bussi vaja 
print("Busse vaja:",bus)
#7. Kui palju on reisijaid viimases bussis kasutades if/else, kui jääks peaks olema 0 läheb bussi kohtade arv, kui ei ole läheb jääk mis arvutatakse #4    
if inimesed == 0:
    print("Viimases bussis reisijaid:",b)
else:
    print("Viimases bussis reisijaid:",inimesed)