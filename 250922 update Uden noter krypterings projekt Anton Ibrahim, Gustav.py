def lavKryptedList(string):
    liste = []
    for i in string: 
        liste.append(ord(i)) 
    return liste 

def kryptering(kryptKey,tekst):
    kryptedTekstString = "" 

    for  i in range(1, len(tekst)+1): 
        kryptedTekst = kryptKey[x-1] + tekst[i-1] 
        kryptedTekstString += chr(kryptedTekst) 
    print (kryptedTekstString) 
    return lavKryptedList(kryptedTekstString) 

def deKryption(kryptKeyAscii,kryptedTekst): 
    deKryptedTekstString = "" 
    
    for  i in range(1, len(kryptedTekst)+1):
        x = i % len(kryptKeyAscii) 
        deKryptedTekst = kryptedTekst[i-1]-kryptKeyAscii[x-1]
        deKryptedTekstString += chr(deKryptedTekst) 
    print (deKryptedTekstString) 

def kryptOrDekrypt(valgKryptOrDekrypt): 
    kryptDone = False
    if  valgKryptOrDekrypt == "k": 
        tekstList = lavKryptedList(input("hvad vil du kryptere: ")) 
        kryptKey = lavKryptedList(input("din personlige krypt key: "))
        kryptedString = kryptering(kryptKey, tekstList) 
        kryptDone = True 

    if valgKryptOrDekrypt == "d" or kryptDone == True:
        if kryptDone == False: 
            kryptedString = lavKryptedList(input("Hvad er den krypterede tekst? "))
        opLåsNøgle = lavKryptedList(input("Hvad er nøglen? ")) 
        deKryption(opLåsNøgle, kryptedString)
    else:
        print("Fejl, prøv igen")
        kryptOrDekrypt(input("Vil du kryptere eller dekryptere? (k/d): ")) 

kryptOrDekrypt(input("Vil du kryptere eller dekryptere? (k/d): ")) 