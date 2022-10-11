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
 
   naamantwoord=input('Geef een coureurs naam op\n\n')
   check_valide_driveraam=is_valide_drivernaam(naamantwoord)
   if check_valide_driveraam:

     print('\n\nIts lights out and away we go!\nGeef bij iedere vraag het juiste antwoord(GEEN HOOFDLETTERS).\n\n')

     antwoord=input('Vraag 1: Welke coureur was in het 2008 kampioenschap voor 30 seconden kampioen?\n\n')
     if antwoord.lower()=='felippe massa' or antwoord.lower()=='felippe massa':
        punten += 1
        print('\n\nMassa was voor maar 30 sec een kampioen, helaas had Hamilton iemand last minute ingehaald waardoor hij kampioen werd. Goed gedaan!\n\n')
     else:
        print('Dat is fout!\n\n')
 
     antwoord=input('Vraag 2: Hoeveel wereldkampioenen hebben we nu op de grid?\n\n')
     if antwoord.lower()=='4':
        punten += 1
        print('\n\nDe huidige coureurs zijn: Fernando Alonso, Max Verstappen, Sebastian Vettel en Lewis Hamilton. Goed gedaan!\n\n')
     else:
        print('Dat is fout!\n\n')

     antwoord=input('Vraag 3: Wat was het belangrijke onderdeel van de Brawn GP auto waardoor het team de beide kampioenschappen heeft weten te winnen 2009?(GEEF ANTWOORD IN HET ENGELS)\n\n')
     if antwoord.lower()=='double diffuser' or antwoord.lower()=='double diffuser':
        punten += 1
        print('\n\nDit onderdeel was een van de grootste technologische inovaties ooit. Dit leverde Jenson Button zijn eerste en enige kampioenschap op. Goed gedaan!\n\n')
     else:
        print('Dat is fout!\n\n')

     antwoord=input('Vraag 4: In de Formule 1 heeft het sigaretten merk Marlboro 4 teams gesponsord. Welk team heeft dit merk naast Ferrari, Mclaren en Iso-Marlboro op hun auto gehad? \n\n(a)BRM\n(b)Jordan\n(c)Williams\n(d)Toyota\n\n')
     if antwoord.lower()=='a':
        punten += 1
        print('\n\nBRM heeft tijdens hun tijd met de sponsor een bijna identieke livery gehad die de Mclaren een aantal jaar later heeft gebruikt. Goed gedaan!\n\n')
     else:
        print('Dat is fout!\n\n')

     antwoord=input('Vraag 5: Wie is de eerste Finse wereldkampioen?\n\n')
     if antwoord.lower()=='keke rosberg' or antwoord.lower()=='keke rosberg':
        punten += 1
        print('\n\nKeke Rosberg werd in 1982 kampioen, later heeft zijn zoon Nico Rosberg in 2016 onder Duitse nationaliteit ook een kampioenschap gewonnen. Goed gedaan!')
     else:
        print('Dat is fout!\n\n')

     antwoord=input('Vraag 6: Wie was de laatste wereldkampioen met Ferrari?\n\n')
     if antwoord.lower()=='kimi raikkonen' or antwoord.lower()=='kimi raikkonen':
        punten += 1
        print('\n\nKimi Raikkönen heeft in het 2007 seizoen zijn eerste en laatste kampioenschap gewonnen. Hiermee heeft hij gedaan wat Felippe Massa vorig seizoen niet heeft weten te doen. Goed gedaan!\n\n')
     else:
        print('Dat is fout!\n\n')

     antwoord=input('Vraag 7: Welke coureur wordt geschat als de beste allertijde? \n\n(a)Niki Lauda\n(b)Michael Schumacher\n(c)Ayrton Senna\n(d)Lewis Hamilton\n\n')
     if antwoord.lower()=='c':
        punten += 1
        print('\n\nDit is overduidelijk de beste coureur! Goed gedaan!\n\n')
     elif antwoord.lower()=='b':
         print('\n\nDeze coureur is ook een van de beste. Goed gedaan!\n\n')
     else:
        print('Dat is fout!\n\n')

     antwoord=input('Vraag 8: Wie heeft de snelste ronde ooit neergezet?\n\n')
     if antwoord.lower()=='juan pablo montoya' or antwoord.lower()=='juan pablo montoya':
        punten += 1
        print('\n\nJuan heeft op het circuit Monza de snelste ronde neergezet tijdens de kwalificatie in 2004. Goed gedaan!\n\n')
     else:
        print('Dat is fout!\n\n')

     antwoord=input('Vraag 9: In 1968, het Lotus team was het eerste team die sponsors op hun autos had. Wie sponsorde hun? \n(a)Marlboro\n(b)John Player Special\n(c)Elf\n(d)Gold Leaf\n\n')
     if antwoord.lower()=='b':
        punten += 1
        print('\n\nLotus was de allereeste die een sponsor had. Dit zorgde ervoor dat meer teams sponsors kregen en zorgt er zelfs nu nog voor dat er elk jaar ieder team een unieke auto heeft. Goed gedaan!\n\n')
     else:
        print('Dat is fout!\n\n')

     antwoord=input('Vraag 10: In de Grand Prix van Amerika in 2005 starte de minste autos ooit. Hoeveel autos starte er toen?\n\n')
     if antwoord.lower()=='6':
        punten += 1
        print('\n\nDoor de grove grond van de Nascar baan slijte de michellin banden van elk team te snel waardoor ze niet konden rijden. De overige 3 teams die Bridgestone banden hadden konden wel lang rijden omdat deze een langere levensduur hadden dan de Michellin banden. Goed gedaan!\n\n')
     else:
        print('Dat is fout!\n\n')
    
     cijfer = round(float(10/aantal_vragen*punten), 1)
     print('\n\nJe hebt de race gefinisht, je voorlopige gridplek is:'+str(cijfer)+'.\n\n')
     if punten >= 2: print('\n\nGreat stuff! Return to the pits.\n\n')
     else: print('\n\nEngine off! Are you ok?\n\n')

   else:
      print('false')

elif antwoord.lower()=='nee':
 print('\n\nJe vind de baan nog te nat voor slicks.\nEerst nog wachten tot het droog is.')
