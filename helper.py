def som(inkomsten):
    totaal = 0
    for item, bedrag in inkomsten.items():
        totaal += bedrag
    return totaal