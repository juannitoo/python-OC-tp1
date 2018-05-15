# -*-coding:Utf-8 -*

import os
from random import randrange
from math import ceil

argent_joueur = 100

print('Bienvenue au Zcasino. N\'appuyez surtout pas sur q pour sortir et donnez nous tout votre argent')

while argent_joueur > 0:

    tirage_roulette = randrange(50)

    print('Il vous reste ',argent_joueur,'$ pour miser')
    numero_mise = int(input('  On joue à la roulette. Sur quel numéro entre 0 et 49 voulez-vous miser ?'))
    mise = int(input('  Combien d\'argent voulez-vous miser ?'))


    # faudrait rajouter 1 condition pour s'assurer que nos input sont bien des nbres
    if numero_mise >= 0 and numero_mise <= 49 and mise > 0 and mise <= argent_joueur:

        if numero_mise % 2 == 0:
            print('  Vous misez ',mise,'$ sur le ',numero_mise,' noir pair')
        else:
            print('  Vous misez',mise,'$ sur le ',numero_mise,' impair rouge')

        if tirage_roulette % 2 == 0:
            print('  Croupier : rien ne va plus. Le ',tirage_roulette,' - noir pair')
            if  numero_mise % 2 == 0:
                print('  vous récupérez ',ceil(mise * 0.5),'$')
                argent_joueur = argent_joueur + ceil(mise * 0.5)
        else:
            print('  Croupier : rien ne va plus. Le ',tirage_roulette,' - rouge impair')
            if numero_mise % 2 != 0:
                print('  vous récupérez ',ceil(mise * 0.5),'$')
                argent_joueur = argent_joueur + ceil(mise * 0.5)

        if numero_mise == tirage_roulette:
            print('Quelle chance ! Vous avez gagné ',mise*3,'$ ! Mais ne partez pas sans avoir tout dépenser !')
            argent_joueur = argent_joueur + ceil(mise * 3)
        else:
            print('  Perdu !')
            argent_joueur -= mise
        
    else:
        print('On mise sur des numéros entre 0 et 49 et SURTOUT on fait pas crédit !')


    if argent_joueur == 0:
        print('C\'est bon, on vous a plumé, vous pouvez partir en appuyant sur "q"' )

    if mise == "q" or numero_mise == "q":
        exit()


os.system("pause")