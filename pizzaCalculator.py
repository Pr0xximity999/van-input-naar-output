meerpizzas = False
nietMeerPizzas = False
groottePrijs = 0.0
toppingAantallen = list()
pizzaGroepInformatie = list()
verschillendePizzaAantallen = list()
enkelPizzaPrijs = 0.0
toppingPrijsChampignon = 0.05
toppingPrijsKaas = 0.15
toppingPrijsPepperoni = 0.50
toppingPrijsAnnanas = 0.20
toppingPrijsWater = 0.01
totalePizzaPrijs = 0

print("Hallo, en welkom bij mijn pizzawinkel!")

while True:
    
    aantalChampignon = 0.0
    aantalKaas = 0.0
    aantalPepperoni = 0.0
    aantalAnnanas = 0.0
    aantalWater = 0.0
    if nietMeerPizzas == True: break
    meerpizzas = False
    print("--------------------")
    print("      klein|€ 3,00  |")
    print("     medium|€ 6,50  |")
    print("      groot|€ 10,00 |")
    print("extra-large|€ 13,50 |")
    print(" gigantisch|€ 15,00 |")
    print("--------------------")
    print("Welke grootte pizza wilt u hebben?")
    #Vraagt hoe groot de pizzabodem is
    groottePizza = input()

    if groottePizza == "klein":
        groottePizza = "kleine"
        groottePrijs = 3.0

    elif groottePizza == "medium":
        groottePizza = "medium"
        groottePrijs = 6.50

    elif groottePizza == "groot":
        groottePizza = "grote"
        groottePizza = 6.10

    elif groottePizza == "extra-large" or groottePizza == "extra large":
        groottePizza = "extra large"
        groottePrijs = 13.50

    elif groottePizza == "gigantisch":
        groottePrijs = "gigantische"
        groottePrijs = 15.00

    #laat de keuze van de toppings zien en vraagt hoeveel pizza's je er mee wilt

    while True:
        if meerpizzas == True: break
        if nietMeerPizzas == True: break
        print("Welke toppings wil je er op?")
        print("--------------------")
        print(" prijs per stuk/gram|")
        print("--------------------")
        print(" champignon|€ 0.05  |")
        print("       kaas|€ 0.15  |")
        print("  pepperoni|€ 0.50  |")
        print("    annanas|€ 0.20  |")
        print("      water|€ 0.01  |")
        print("--------------------")

        gekozenTopping = input()


        #De champignon
        if gekozenTopping == "champignon":
            gekozenTopping = "champignons"
            aantalChampignon += float(input("Hoeveel " + gekozenTopping + " wil je hebben op je pizza? "))
            enkelPizzaPrijs += aantalChampignon * toppingPrijsChampignon + groottePrijs

            meerToppings = input("Wilt u meer toppings hebben? y/n ")
            if meerToppings == "y": 
                continue

            else:
                #Berekend de prijs van de groep pizza's
                aantalPizzas = float(input("Hoeveel pizza's wil u hiermee hebben? "))
                groepsPizzaPrijs = enkelPizzaPrijs * aantalPizzas

                #Voegt de pizzagroep en al de informatie toe een een lijst
                toppingAantallen
                pizzaGroepInformatie.append(aantalPizzas)
                pizzaGroepInformatie.append(groepsPizzaPrijs)
                pizzaGroepInformatie.append(aantalChampignon)
                pizzaGroepInformatie.append(aantalKaas)
                pizzaGroepInformatie.append(aantalPepperoni)
                pizzaGroepInformatie.append(aantalAnnanas)
                pizzaGroepInformatie.append(aantalWater)
                pizzaGroepInformatie.append(groottePrijs)

                meerpizzas = input("Wilt u meer pizza's hebben? y/n ")
                if meerpizzas == "y":
                    meerpizzas = True
                    verschillendePizzaAantallen.append(pizzaGroepInformatie)
                    continue
                else:
                    nietMeerPizzas = True
                    verschillendePizzaAantallen.append(pizzaGroepInformatie)
                    continue
                


        #De kaas
        elif gekozenTopping == "kaas":
            gekozenTopping = "gram kaas"
            aantalKaas += float(input("Hoeveel " + gekozenTopping + " wil je hebben op je pizza? "))
            enkelPizzaPrijs += aantalChampignon * toppingPrijsKaas + groottePrijs

            meerToppings = input("Wilt u meer toppings hebben? y/n ")
            if meerToppings == "y": 
                continue

            else:
                #Berekend de prijs van de groep pizza's
                aantalPizzas = float(input("Hoeveel pizza's wil u hiermee hebben? "))
                groepsPizzaPrijs = enkelPizzaPrijs * aantalPizzas

                #Voegt de pizzagroep en al de informatie toe een een lijst
                toppingAantallen
                pizzaGroepInformatie.append(aantalPizzas)
                pizzaGroepInformatie.append(groepsPizzaPrijs)
                pizzaGroepInformatie.append(aantalChampignon)
                pizzaGroepInformatie.append(aantalKaas)
                pizzaGroepInformatie.append(aantalPepperoni)
                pizzaGroepInformatie.append(aantalAnnanas)
                pizzaGroepInformatie.append(aantalWater)
                pizzaGroepInformatie.append(groottePrijs)

                meerpizzas = input("Wilt u meer pizza's hebben? y/n ")
                if meerpizzas == "y":
                    meerpizzas = True
                    verschillendePizzaAantallen.append(pizzaGroepInformatie)
                    continue
                else:
                    nietMeerPizzas = True
                    verschillendePizzaAantallen.append(pizzaGroepInformatie)
                    continue


        #De pepperoni
        elif gekozenTopping == "pepperoni":
            gekozenTopping = "pepperoni"
            aantalPepperoni += float(input("Hoeveel " + gekozenTopping + " wil je hebben op je pizza? "))
            enkelPizzaPrijs += aantalChampignon * toppingPrijsPepperoni + groottePrijs

            meerToppings = input("Wilt u meer toppings hebben? y/n ")
            if meerToppings == "y": 
                continue

            else:
                #Berekend de prijs van de groep pizza's
                aantalPizzas = float(input("Hoeveel pizza's wil u hiermee hebben? "))
                groepsPizzaPrijs = enkelPizzaPrijs * aantalPizzas

                #Voegt de pizzagroep en al de informatie toe een een lijst
                toppingAantallen
                pizzaGroepInformatie.append(aantalPizzas)
                pizzaGroepInformatie.append(groepsPizzaPrijs)
                pizzaGroepInformatie.append(aantalChampignon)
                pizzaGroepInformatie.append(aantalKaas)
                pizzaGroepInformatie.append(aantalPepperoni)
                pizzaGroepInformatie.append(aantalAnnanas)
                pizzaGroepInformatie.append(aantalWater)
                pizzaGroepInformatie.append(groottePrijs)              

                meerpizzas = input("Wilt u meer pizza's hebben? y/n ")
                if meerpizzas == "y":
                    meerpizzas = True
                    verschillendePizzaAantallen.append(pizzaGroepInformatie)
                    continue
                else:
                    nietMeerPizzas = True
                    verschillendePizzaAantallen.append(pizzaGroepInformatie)
                    continue


        #De annanas
        elif gekozenTopping == "annanas":
            gekozenTopping = "annanas"
            aantalAnnanas += float(input("Hoeveel " + gekozenTopping + " wil je hebben op je pizza? "))
            enkelPizzaPrijs += aantalChampignon * toppingPrijsAnnanas + groottePrijs

            meerToppings = input("Wilt u meer toppings hebben? y/n ")
            if meerToppings == "y": 
                continue

            else:
                #Berekend de prijs van de groep pizza's
                aantalPizzas = float(input("Hoeveel pizza's wil u hiermee hebben? "))
                groepsPizzaPrijs = enkelPizzaPrijs * aantalPizzas

                #Voegt de pizzagroep en al de informatie toe een een lijst
                toppingAantallen
                pizzaGroepInformatie.append(aantalPizzas)
                pizzaGroepInformatie.append(groepsPizzaPrijs)
                pizzaGroepInformatie.append(aantalChampignon)
                pizzaGroepInformatie.append(aantalKaas)
                pizzaGroepInformatie.append(aantalPepperoni)
                pizzaGroepInformatie.append(aantalAnnanas)
                pizzaGroepInformatie.append(aantalWater)
                pizzaGroepInformatie.append(groottePrijs)

                meerpizzas = input("Wilt u meer pizza's hebben? y/n ")
                if meerpizzas == "y":
                    meerpizzas = True
                    verschillendePizzaAantallen.append(pizzaGroepInformatie)
                    continue
                else:
                    nietMeerPizzas = True
    
                    verschillendePizzaAantallen.append(pizzaGroepInformatie)
                    continue

        #Het water
        elif gekozenTopping == "water":
            gekozenTopping = "gram water"
            aantalWater += float(input("Hoeveel " + gekozenTopping + " wil je hebben op je pizza? "))
            enkelPizzaPrijs += aantalChampignon * toppingPrijsWater + groottePrijs

            meerToppings = input("Wilt u meer toppings hebben? y/n ")
            if meerToppings == "y": 
                continue

            else:
                #Berekend de prijs van de groep pizza's               
                aantalPizzas = float(input("Hoeveel pizza's wil u hiermee hebben? "))
                groepsPizzaPrijs = enkelPizzaPrijs * aantalPizzas

                #Voegt de pizzagroep en al de informatie toe een een lijst
                toppingAantallen
                pizzaGroepInformatie.append(aantalPizzas)
                pizzaGroepInformatie.append(groepsPizzaPrijs)
                pizzaGroepInformatie.append(aantalChampignon)
                pizzaGroepInformatie.append(aantalKaas)
                pizzaGroepInformatie.append(aantalPepperoni)
                pizzaGroepInformatie.append(aantalAnnanas)
                pizzaGroepInformatie.append(aantalWater)
                pizzaGroepInformatie.append(groottePrijs)

                meerpizzas = input("Wilt u meer pizza's hebben? y/n")
                if meerpizzas == "y":
                    meerpizzas = True
                    verschillendePizzaAantallen.append(pizzaGroepInformatie)
                    continue
                else:
                    nietMeerPizzas = True
                    verschillendePizzaAantallen.append(pizzaGroepInformatie)
                    continue

#Berekend de prijs van alle pizza's
for x in verschillendePizzaAantallen:
    totalePizzaPrijs += x[1]
    totalePizzaPrijs += x[2] * toppingPrijsChampignon
    totalePizzaPrijs += x[3] * toppingPrijsKaas
    totalePizzaPrijs += x[4] * toppingPrijsPepperoni
    totalePizzaPrijs += x[5] * toppingPrijsAnnanas
    totalePizzaPrijs += x[6] * toppingPrijsWater

print("De totale prijs van uw pizza('s) is €" + str(totalePizzaPrijs))
#Leest de prijzen op van de groepen pizza en laat per groep het beleg zien
print("Uw pizzalijst:")
for x in verschillendePizzaAantallen:
    print("|" + str(x[0]) + " Pizza's met:")
    print("|" + str(x[2]) + " champignons,")
    print("|" + str(x[3]) + " gram kaas,")
    print("|" + str(x[4]) + " stukken pepperoni,")
    print("|" + str(x[5]) + " stukken annanas,")
    print("|" + str(x[6]) + " gram water")
    print("| ten waarde van €" + str(x[1] + x[2] * toppingPrijsChampignon + x[3] * toppingPrijsKaas + x[4] * toppingPrijsPepperoni + x[5] * toppingPrijsAnnanas + x[6] * toppingPrijsWater))
    print("----------------------------")
print("Dit allemaal bij elkaar kost in totaal €" + str(totalePizzaPrijs))
print("Bedankt voor uw bestelling!")