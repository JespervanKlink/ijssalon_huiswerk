from algemene_functies import mijn_functie_2(korte_lijst)

def mijn_functie_2(getallen):
    getallen = {
        "12.3 -" : "15,9,36,4",
        "12.2 -" : "14,10,24,6",
        "10.5 -" : "15,5,50,2",
        "100.2 -" : "120,80,2000,5"
    }
    for k,v in getallen.items():
        print(k,v)
mijn_functie_2("getallen")