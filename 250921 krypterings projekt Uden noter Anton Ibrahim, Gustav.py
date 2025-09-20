def lavKryptedList(string):
    liste = [] 
    for i in string: 
        liste.append(ord(i)) 
    return liste

def kryptering(kryptKey,tekst):
    kryptedTekstString = "" 
    for  i in range(1, len(tekst)+1):
        x = i % len(kryptKey) 
        kryptedTekst = kryptKey[x-1] + tekst[i-1] 
        kryptedTekstString += chr(kryptedTekst) 
    
    print (kryptedTekstString) 
    return lavKryptedList(kryptedTekstString) 

def deKryption(kryptKey,kryptedTekst):
    deKryptedTekstString = "" 
    
    for  i in range(1, len(kryptedTekst)+1):
        x = i % len(kryptKey) 
        deKryptedTekst = kryptedTekst[i-1]-kryptKey[x-1]
        if deKryptedTekst < 0:
            deKryptedTekst += 256
        
        deKryptedTekstString += chr(deKryptedTekst) 
    
    print (deKryptedTekstString)

kryptOrDekrypt = input("Vil du kryptere eller dekryptere? (k/d): ")
kryptDone = False
if  kryptOrDekrypt == "k":
    tekstList = lavKryptedList(input("hvad vil du kryptere: "))
    kryptKey = lavKryptedList(input("din personlige krypt key: "))
    kryptedString = kryptering(kryptKey, tekstList)
    kryptDone = True


if kryptOrDekrypt == "d" or kryptDone == True:
    if kryptDone == False:
        kryptedString = lavKryptedList(input("Hvad er den krypterede tekst? "))
    opLåsNøgle = lavKryptedList(input("Hvad er nøglen? ")) 
    deKryption(opLåsNøgle, kryptedString)
else:
    print("Fejl, prøv igen")
