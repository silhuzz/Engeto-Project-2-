#PISKVORKY 2.0
# by Tomas S


def zadani_hrace():
    while True:
        pole = input("Vyber si velikost hracího pole.\nVelikost musí být mezi 3 - 100")
        if not pole.isdecimal():
            print("Zadej celé číslo")
            continue
        if not (int(pole) < 3) and not (int(pole) > 100):
            nakolik = int(input("Chceš hrát na 3 nebo 5 výherných?"))
            if nakolik > int(pole):
                print("Máš moc malé hrací pole na to.")
                continue
            if (nakolik == 3) or (nakolik == 5):
                print(pole, nakolik)
                return pole, nakolik
            else:
                print("Zadej bud 3 nebo 5!")
                continue
        else:
            print("Zadej číslo mezi 3 až 100. (např 5, 10, 12 atd.")
            continue


def matice_puvodni_stav(pole, matice):
    for i in range(0, len(matice), pole):
        rozdeleni = matice[i:i + pole]
        print("|".join(rozdeleni))
        radky = "- " * (pole)
        print(radky)


def vykresli_matici(pole, matice):
    for i in range(0, len(matice), pole):
        rozdeleni = matice[i:i + pole]
        print("|".join(rozdeleni))
        radky = "- " * (pole)
        print(radky)


def zadani_pozice(pole, matice, symbol):
    while True:
        text = ""
        if symbol == 1:
            symbol = "o"
        elif symbol == 2:
            symbol = "x"
        pozice = input("Hráč |" + symbol + "| zadej pozici mezi 1 až " + str(pole * pole))
        if pozice.isdecimal():
            if int(pozice) >= 1 and int(pozice) <= pole * pole:
                pozice = int(pozice) - 1
                if ("x" in matice[pozice]) or ("o" in matice[pozice]):
                    print("Takhle piškvorky nefungujou, zvol jiné pole.")
                else:
                    matice[pozice] = symbol
                    return matice
        else:
            print("Zadej celé číslo mezi 1 až " + str(pole * pole))
            continue


def vyhra_radky(pole, matice, nakolik):
    hrac1 = ["x"] * nakolik
    hrac2 = ["o"] * nakolik
    for i in range(0, len(matice), pole):
        rozdeleni = matice[i:i + pole]
        if (''.join(hrac1) in ''.join(rozdeleni)):
            print("Vyhrál hráč 1! Gratulace!")
            return True
        elif (''.join(hrac2) in ''.join(rozdeleni)):
            print("Vyhrál hráč 2! Gratulace!")
            return True


def vyhra_sloupce(pole, matice, nakolik):
    hrac1 = ["x"] * nakolik
    hrac2 = ["o"] * nakolik
    zacatek = 0
    while zacatek < pole:
        rozdeleni = matice[zacatek::pole]
        if (''.join(hrac1) in ''.join(rozdeleni)):
            print("Vyhrál hráč 1! Gratulace!")
            return True
        elif (''.join(hrac2) in ''.join(rozdeleni)):
            print("Vyhrál hráč 2! Gratulace!")
            return True
        else:
            zacatek += 1


def vyhra_diagonal1(pole, matice, nakolik):
    if nakolik == 3:
        zacatek = 2
        konec = (pole * 2)
    elif nakolik == 5:
        zacatek = 4
        konec = ((pole - nakolik) * (nakolik) + 20)
        # dospel jsem k tomu matematicky,
        # nejnizsi mozny konecny index je 20+1 kde pole je 5x5 a hraje se na 5 vyhernych,
        # pri kazdem dalsi zvetseni hraciho pole dojde k navýšenní posledního indexu o 5
    counter = 1
    skok = nakolik - 1
    hops = (pole - nakolik) + 1
    skip = pole - 1
    seznam_diagonal1 = []
    for i in range(len(matice)):
        if (i % hops == 0) and (i != 0):
            zacatek += skok
            counter += skok
        bonbon = matice[zacatek:((konec) + counter):skip]
        seznam_diagonal1.append(bonbon)
        zacatek += 1
        counter += 1
    hrac1 = ["x"] * nakolik
    hrac2 = ["o"] * nakolik
    for z in seznam_diagonal1:
        if hrac1 == z:
            print("Vyhrál hráč 1! Gratulace!")
            return True
        elif hrac2 == z:
            print("Vyhrál hráč 2! Gratulace!")
            return True


def vyhra_diagonal2(pole, matice, nakolik):
    if nakolik == 3:
        konec = (pole * 2) + 2
    elif nakolik == 5:
        konec = ((pole * 4) + 4)
    counter = 1
    skok = nakolik - 1
    hops = (pole - nakolik) + 1
    skip = pole + 1
    zacatek = 0
    seznam_diagonal2 = []
    for i in range(len(matice)):
        if (i % hops == 0) and (i != 0):
            zacatek += skok
            counter += skok
        bonbon = matice[zacatek:((konec) + counter):skip]
        seznam_diagonal2.append(bonbon)
        zacatek += 1
        counter += 1
    hrac1 = ["x"] * nakolik
    hrac2 = ["o"] * nakolik
    for z in seznam_diagonal2:
        if hrac1 == z:
            print("Vyhrál hráč 1! Gratulace!")
            return True
        elif hrac2 == z:
            print("Vyhrál hráč 2! Gratulace!")
            return True


def main():
    intro = """===========================\nWelcome to Tic Tac Toe\n
     GAME RULES:\n
     Each player can place one mark per turn your selected grid\n
     The WINNER is who succeeds in placing three of their marks in a\n
     * horizontal,\n
     * vertical or\n
     * diagonal row\n
     ==========================="""
    print(intro)
    user_info = zadani_hrace()
    pole = int(user_info[0])
    nakolik = int(user_info[1])
    matice = [" "] * pole * pole
    game_on = True
    tah = 1
    matice_puvodni_stav(pole, matice)
    while game_on:
        symbol = 2 if tah % 2 == 0 else 1
        matice = zadani_pozice(pole, matice, symbol)
        if (vyhra_radky(pole, matice, nakolik)
                or vyhra_sloupce(pole, matice, nakolik)
                or vyhra_diagonal1(pole, matice, nakolik)
                or vyhra_diagonal2(pole, matice, nakolik)):
            game_on = False
        elif (tah == pole * pole):
            game_on = False
            rozhodnuti = input("Nikdo nevyhrál, chcete hrát znovu? Napiš: Y/N").lower()
            if rozhodnuti == "y":
                game_on = False
                main()
            elif rozhodnuti == "n":
                game_on = False
                print("Díky za hru")
                break
            else:
                print("Zadej Y pro pokračovaní a N pro konec.")
                continue
        vykresli_matici(pole, matice)
        tah += 1


if __name__ == "__main__":
    main()