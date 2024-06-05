from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting = (float(prijs) * 0.9)
    uitvoer = (f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting}")
    return uitvoer
aanbieding = aanbieding_1("aardbei", "4", "3.60")
print(aanbieding)

omzet = (220,430,125,160,205,90,345)

def inkomsten_totaal(inkomsten):
    inkomsten = sum(omzet)
    return inkomsten
inkomsten = inkomsten_totaal(sum)
print(inkomsten)

def inkomsten_totaal(uitvoer):
    totaal = sum(omzet)
    bedrag = totaal - (round(float(totaal) / 1.09))
    uitvoer = (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden")
    print(uitvoer)
inkomsten_totaal("uitvoer")

def laag_en_hoog(mijn_lijst):
    mijn_lijst = min(omzet), max(omzet)
    print(mijn_lijst)
laag_en_hoog("mijn_lijst")

def gemiddelde(mijn_lijst):
    bedrag = round(sum(omzet) / len(omzet))
    mijn_lijst = (f"De gemiddelde inkomsten deze week zijn {bedrag} euro.")
    print(mijn_lijst)
gemiddelde("mijn_lijst")

def meervoudig(invoer_lijst):
    invoer_lijst = min(omzet), max(omzet)
    print(invoer_lijst)
meervoudig("invoer_lijst")

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
combinatie("invoer_lijst_2")

