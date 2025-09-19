# Modulo værdi (brug af %). tæl op indtils du når et tal og så start forfra.

def lavKryptedList(string): # Etablere en funktion der laver en sting om til en liste med ascii værdier.
    liste = [] # laver en tom liste.
    for i in string: # for hvert bogstav i strengen .
        liste.append(ord(i)) # tilføj ascii værdien af bogstavet til listen.
    return liste # returner listen.

def kryptering(kryptKey,tekst): # funktion der krypterer teksten.
    kryptedTekstString = "" # laver en tom string til den krypterede tekst.

    for  i in range(1, len(tekst)+1): # for hvert tal i intervallet fra 1 til længden af teksten + 1. (plusser med 1 fordi ellers virker modulo ikke i den sammenhæng jeg vil bruge det til)
        x = i % len(kryptKey) # får modulo værdien af i ud fra længden af krypterings nøglen.
        kryptedTekst = kryptKey[x-1] + tekst[i-1] # lægger ascii værdien af bogstavet i teksten sammen med ascii værdien af bogstavet i krypterings nøglen. (x-1 og i-1 fordi lister starter ved 0)
        kryptedTekstString += chr(kryptedTekst) # tilsætter det krypterede bogstav til den krypterede tekst string vi lavede i starten af funktionen.
    
    print (kryptedTekstString) # viser den krypterede tekst til brugeren.
    return lavKryptedList(kryptedTekstString) # returner den krypterede tekst som en liste med ascii værdier.

def deKryption(kryptKey,kryptedTekst): # funktion der dekrypterer teksten.
    deKryptedTekstString = "" # laver en tom string til den dekrypterede tekst.
    
    for  i in range(1, len(kryptedTekst)+1): # for hvert tal i intervallet fra 1 til længden af den krypterede tekst + 1. (plusser med 1 fordi ellers virker modulo ikke i den sammenhæng jeg vil bruge det til)
        x = i % len(kryptKey) # får modulo værdien af i ud fra længden af krypterings nøglen.
        deKryptedTekst = kryptedTekst[i-1]-kryptKey[x-1] # trækker ascii værdien af bogstavet i krypterings nøglen fra ascii værdien af bogstavet i den krypterede tekst. (x-1 og i-1 fordi lister starter ved 0)
        deKryptedTekstString += chr(deKryptedTekst) # tilsætter det dekrypterede bogstav til den dekrypterede tekst string vi lavede i starten af funktionen.
    
    print (deKryptedTekstString) # viser den dekrypterede tekst til brugeren.

tekstList = lavKryptedList(input("hvad vil du kryptere: ")) # beder brugeren om at indtaste en tekst der skal krypteres og laver den om til en liste med ascii værdier.
kryptKey = lavKryptedList(input("din personlige krypt key: ")) # beder brugeren om at indtaste en krypterings nøgle og laver krypterings nøglen om til en liste med ascii værdier.
kryptedString = kryptering(kryptKey, tekstList) # kalder krypterings funktionen og gemmer den krypterede tekst som en liste med ascii værdier.

opLåsNøgle = lavKryptedList(input("Hvad er nøglen? ")) # beder brugeren om at indtaste krypterings nøglen for at dekryptere teksten.
deKryption(opLåsNøgle, kryptedString)