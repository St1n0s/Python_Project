print('\n\n\nWelkom bij de Formule 1 Quiz!')

antwoord=input('Ben je klaar om te racen? (ja/nee) :')
punten=0
aantal_vragen=10

def is_valide_drivernaam(drivernaam):
    namen = ['lewis','george','max','sergio','lando','daniel','fernando','esteban','mick','kevin','charles','carlos','sebastian','lance','albon','nicholas','valterri','zhou','pierre','yuki']
    for naam in namen:
        if naam==drivernaam.lower(): 
            return True
    return False

if antwoord.lower()=='ja':
 
   naamantwoord=input('Geef je naam op')
   check_valide_driveraam=is_valide_drivernaam(naamantwoord)
   if check_valide_driveraam:

     print('\n\nIts lights out and away we go!\nGeef bij iedere vraag het juiste antwoord(GEEN HOOFDLETTERS).\n\n')

     antwoord=input('Vraag 1: Welke coureur was in het 2006 kampioenschap voor 30 seconden kampioen?\n')
     if antwoord.lower()=='felippe massa' or antwoord.lower()=='felippe massa':
        punten += 1
        print('goed!')
     else:
        print('fout!')
 
     antwoord=input('Vraag 2: Hoeveel wereldkampioenen hebben we nu op de grid?\n')
     if antwoord.lower()=='4':
        punten += 1
        print('goed')
     else:
        print('fout')

     antwoord=input('Vraag 3: Wat was het belangrijke onderdeel van de Brawn GP auto waardoor het team de beide kampioenschappen heeft weten te winnen 2009?(GEEF ANTWOORD IN HET ENGELS)\n')
     if antwoord.lower()=='double diffuser' or antwoord.lower()=='double diffuser':
        punten += 1
        print('goed')
     else:
        print('fout')

     antwoord=input('Vraag 4: In de Formule 1 heeft het sigaretten merk Marlboro 4 teams gesponsord. Welk team heeft dit merk naast Ferrari, Mclaren en Iso-Marlboro op hun auto gehad? \n\n(a)BRM\n(b)Jordan\n(c)Williams\n(d)Toyota')
     if antwoord.lower()=='a':
        punten += 1
        print('goed')
     else:
        print('fout')

     antwoord=input('Vraag 5: Wie is de eerste Finse wereldkampioen?\n')
     if antwoord.lower()=='keke rosberg' or antwoord.lower()=='keke rosberg':
        punten += 1
        print('goed')
     else:
        print('fout')

     antwoord=input('Vraag 6: Wie was de laatste wereldkampioen met Ferrari?\n')
     if antwoord.lower()=='kimi raikkonen' or antwoord.lower()=='kimi raikkonen':
        punten += 1
        print('goed')
     else:
        print('fout')

     antwoord=input('Vraag 7: Welke coureur wordt geschat als de beste allertijde? \n\n(a)Niki Lauda\n(b)Michael Schumacher\n(c)Ayrton Senna\n(d)Lewis Hamilton')
     if antwoord.lower()=='c' or antwoord.lower()=='b':
        punten += 1
        print('goed')
     else:
        print('fout')

     antwoord=input('Vraag 8: Wie heeft de snelste ronde ooit neergezet?\n')
     if antwoord.lower()=='juan pablo montoya' or antwoord.lower()=='juan pablo montoya':
        punten += 1
        print('goed')
     else:
        print('fout')

     antwoord=input('Vraag 9: In 1968, het Lotus team was het eerste team die sponsors op hun autos had. Wie sponsorde hun? \n(a)Marlboro\n(b)John Player Special\n(c)Elf\n(d)Gold Leaf\n')
     if antwoord.lower()=='b':
        punten += 1
        print('goed')
     else:
        print('fout')

     antwoord=input('Vraag 10: In de Grand Prix van Amerika in 2005 starte de minste autos ooit. Hoeveel autos starte er toen?\n')
     if antwoord.lower()=='6':
        punten += 1
        print('goed')
     else:
        print('fout')
    
     cijfer = round(float(10/aantal_vragen*punten), 1)
     print('Je hebt de race gefinisht, je voorlopige gridplek is:'+str(cijfer)+'.')
     if punten >= 2: print('Great stuff! Return to the pits.')
     else: print('Engine off! Are you ok?\n\n')

   else:
      print('false')

elif antwoord.lower()=='nee':
 print('Je vind de baan nog te nat voor slicks.\nEerst nog wachten tot het droog is.')
