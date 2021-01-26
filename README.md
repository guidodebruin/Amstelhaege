# Amstelhaege

## Introductie 
Na jarenlang getouwtrek is de knoop eindelijk doorgehakt: er komt een nieuwe woonwijk in de Duivendrechtse polder, net ten noorden van Ouderkerk aan de Amstel. De huisjes zijn bedoeld voor het midden- en bovensegment van de markt, met name expats en hoogopgeleide werknemers actief op de Amsterdamse Zuidas. Omdat de Duivenderechtse polder ooit beschermd natuurgebied was, is de compromis dat er alleen lage vrijstaande woningen komen, om zo toch het landelijk karakter te behouden. Dit, gecombineerd met een aantal strenge restricties ten aanzien van woningaanbod en het oppervlaktewater, maakt het een planologisch uitdagende klus. De gemeente overweegt drie varianten: de 20-huizenvariant, de 40-huizenvariant en de 60-huizenvariant. Er wordt aangenomen dat een huis meer waard wordt naarmate de vrijstand toeneemt, de rekenpercentages zijn per huistype vastgesteld.

De gemeente heeft ons daarom een opdracht gegeven om de wijk te bouwen. Om de wijk in te richten moeten we als eerst een aantal voorspellingen doen. Ons project team, AH, gespecialiseerd in kunstmatige intelligentie ontwerpt realistische simulaties door gebruik te maken van algoritmes. 

### Restricties voor de wijk
- De wijk komt te staan op een stuk land van 180x160 meter (breed x diep).
- Het aantal woningen in de wijk bestaat voor 60% uit eengezinswoningen, 25% uit bungalows en 15% uit maisons.
- De huizen moeten voldoen aan hun verplichte vrijstand
- De verplichte vrijstand voor iedere woning moet binnen de kaart vallen. Overige vrijstand mag buiten de kaart worden meegerekend.
- De wijk bestaat voor een deel uit oppervlaktewater. Huizen mogen niet op het water worden geplaatst, maar hun vrijstand mag daar   wel op vallen (zowel de verplichte als die voor de waarde berekening).

## Vereisten
- Github 
- Python 3
- Matplotlib
- Shapely

## Installatie
```
pip3 install -r requirements.txt

```

## Gebruik 
- python3 main.py < area_no > < variant >
- Hier kiest de gebruiker welke area hij/zij wilt gebruiken. Keuze uit: (area_1, area_2, area_3) (20, 40, 60)
- Hier kiest de gebruiker welke algoritme hij/zij wilt gebruiken. Keuze: 1, 2 , 3
#### Voorbeeld
```
>>> python3 main.py area_1 40
Choose the algorithm with which you want to perform the calculation
Algorithmes available: Randomstate = 1, Hill Climber = 2, Simulated Annealing = 3
>>> Please choose your algorithm by entering the corresponding number: 2 
```

## Algoritmes

### Randomstate
Bij het Random-algoritme worden huizen willekeurig op de kaart geplaatst met de voorwaarde dat de huizen niet overlappen met het water en/of met elkaar. Verder moeten de huizen binnen de grenzen van het kaart blijven, dus een huis mag niet de grens voor een gedeelte raken. 
Bij de random state hillclimber wordt het algoritme een X aantal keer gelooped aan de hand van de ‘input’ functie. Tijdens het loopen worden er diverse random states gegenereerd(vandaar de naam) en berekent het algoritme steeds de totale waarde van het kaart. Als de nieuwe state een hogere waarde heeft dan de huidige state wordt de nieuwe state opgeslagen. Uiteindelijk blijft de state met de hoogste waarde over.

### Hill Climber
De hill climber lijkt een beetje op de stochastische hill climber variant. Hierbij plaatst het algoritme eerst willekeurig de huizen op de kaart. Vervolgens wordt er een willekeurig huis geselecteerd en verschuift het algoritme het huis in een willekeurige richting. Wanneer deze verplaatsing heeft geleid tot een verhoging van de totale prijs van de huizen, blijft deze verandering in stand. Wanneer dit niet het geval is, wordt het huis teruggeplaatst. Door dit proces telkens te herhalen, wordt er op deze manier getracht de hoogste prijs te behalen voor de huizen.


### Simulated Annealing
De algoritme is significant anders dan de vorige algoritme Hill Climber. Simulated Annealing is een effectieve methode voor optimalisatie en is geïnspireerd door het proces van gloeien(annealing) in metaalbewerking. Bij SA wordt er een temperatuur variabele gebruikt om het verwarmingsproces te simuleren. De temperatuur wordt in de eerste instantie hoog ingesteld en vervolgens wordt het langzaam gekoeld terwijl de algoritme wordt uitgevoerd.
Het afkoelen geeft de algoritme de mogelijkheid om uit lokale optimum te springen. Naarmate de temperatuur daalt, wordt de kans groter dat slechtere oplossingen worden geaccepteerd, waardoor de algoritme zich geleidelijk kan concentreren op een deel van het zoekgebied waarin een bijna optimale oplossing gevonden kan worden.


## Team AH
- Allan Duah
- Guido de Bruin
- Manuka Khan




