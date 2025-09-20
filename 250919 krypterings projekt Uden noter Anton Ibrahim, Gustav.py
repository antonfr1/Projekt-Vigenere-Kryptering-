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
        deKryptedTekstString += chr(deKryptedTekst) 
    
    print (deKryptedTekstString)

tekstList = lavKryptedList(input("hvad vil du kryptere: "))
kryptKey = lavKryptedList(input("din personlige krypt key: "))
kryptedString = kryptering(kryptKey, tekstList) 

opLåsNøgle = lavKryptedList(input("Hvad er nøglen? ")) 
deKryption(opLåsNøgle, kryptedString)