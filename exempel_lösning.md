# Facit

### Exercis_one
```
print("Hello World!")
```

### Exercise_two

```
name = input("Skriv ditt namn: ")

print("Hej ", name)

# Alternativt

name = input("Skriv ditt namn: ")

print(f"Hej {name}")

```

### Exercise_three

```

print("Addition " ,53 + 89)
print("Division " ,53 / 89)
print("Division - heltal" ,53 // 89)
print("Subtraktion", 53 - 89)
print("Multiplikation" ,53 * 89)
print("Upphöjt till " ,53 ** 89)
print("Modulus - rest av division " ,53 % 89)

```
### Exercise_four

```

tal1 = "42"
tal2 = 19.8
tal3 = 25

tal1 = int(tal1)
tal2 = int(tal2)
tal2 = str(tal3)

print(tal1)
print(tal2)
print(tal3)

print(type(tal1))
print(type(tal2))
print(type(tal3))

```

### Exercise_five

```

tal = 4.78654
pris = 19.876

print(round(tal))
print(round(pris, 1 ))


```
### Exercise_six

```

tal1 = 53
tal2 = 54

print(tal1 == tal2)
print(tal1 != tal2)

```

### Exercise_seven

```

x = 15

print(x > 10 and x < 20)


```
### Exercise_eight

```

age = int(input("Hur gammal är du ?"))

if age >= 18:
    print("Du får ta körkort")
else:
    print("Du är för ung för att ta körkort")


```
### Exercise_nine

```
lösenord = "python123"

if lösenord == "python123":
    print("Rätt lösenord!")
else:
    print("Fel lösenord!")
```

### Exercise_eleven

```
raknare = 10

while raknare >= 1:

    print(raknare)
    
    raknare = raknare - 1

```

### Exercise_twelve

```

health_points = 100

while health_points > 0:
    print("Player healtpoints: " , health_points)
    health_points = health_points - 20
print("Game Over!")

```


#Övning 6 – Samla XP och levla upp 🎯
Utmaning
Uppgift: Spelaren börjar med 0 XP. Varje uppdrag ger 50 XP. När spelaren når 200 XP ska den levla upp.

Instruktioner
Skapa en variabel som heter xp.

Ge variabeln startvärdet 0.

Skapa en variabel som heter uppdrags_xp.

Ge variabeln värdet 50.

Skapa en while-loop som fortsätter så länge xp är mindre än 200.

Lägg till 50 XP efter varje uppdrag.

Skriv ut hur mycket XP spelaren har.

När spelaren når 200 XP ska du skriva ut "LEVEL UP!".

Förväntad utskrift:

```
text
Du klarade ett uppdrag!
Du har 50 XP

Du klarade ett uppdrag!
Du har 100 XP

Du klarade ett uppdrag!
Du har 150 XP

Du klarade ett uppdrag!
Du har 200 XP
```
LEVEL UP!
Extra utmaning – Skapa ett enkelt textbaserat spel 🎮
Boss level
Nu får du kombinera flera saker du har tränat på.

Uppgift: Skapa ett spel där användaren är en spelare som ska besegra ett monster.

Instruktioner
Spelaren börjar med 100 HP.

Monstret börjar med 100 HP.

Skapa en while-loop som fortsätter så länge både spelaren och monstret har mer än 0 HP.

Låt spelaren attackera monstret och göra 25 skada.

Skriv ut monstrets återstående HP.

Om monstret fortfarande lever ska det attackera spelaren och göra 20 skada.

Skriv ut spelarens återstående HP.

När någon får 0 HP eller mindre ska loopen avslutas.

Kontrollera vem som vann och skriv ut ett passande meddelande.


# Övning 5 – Gissa lösenordet till spelkistan 🔐
Medel
Uppgift: Spelaren hittar en låst skattkista. För att öppna den måste spelaren skriva rätt lösenord.

Lösenordet är dragon.

Instruktioner
Skapa en variabel som heter ratt_losenord.

Spara texten "dragon" i variabeln.

Skapa en variabel som heter gissning.

Ge den ett tomt startvärde, exempelvis "".

Skapa en while-loop som fortsätter så länge gissningen inte är samma som lösenordet.

Be spelaren skriva in ett lösenord.

Spara svaret i gissning.

När spelaren skriver rätt lösenord ska loopen avslutas.

Skriv ut "Skattkistan är upplåst!".

Exempel på körning:

```
text
Skriv lösenordet: sword
Fel lösenord!
Skriv lösenordet: monster
Fel lösenord!
Skriv lösenordet: dragon
Skattkistan är upplåst!
```


# Övning 4 – Boss fight 👹
Medel
Uppgift: Spelaren möter en boss som har 100 HP. Varje attack gör 25 skada.

Instruktioner
Skapa en variabel som heter boss_halsa.

Ge variabeln startvärdet 100.

Skapa en variabel som heter skada.

Ge variabeln värdet 25.

Skapa en while-loop som fortsätter så länge bossens hälsa är större än 0.

Minska bossens hälsa med värdet i skada.

Skriv ut hur mycket hälsa bossen har kvar.

När bossens hälsa når 0 ska du skriva ut "Boss defeated!".

Förväntad utskrift:

```
text
Du attackerar bossen!
Bossens HP: 75
Du attackerar bossen!
Bossens HP: 50
Du attackerar bossen!
Bossens HP: 25
Du attackerar bossen!
Bossens HP: 0
Boss defeated!
```

# Övning 4 – Är du tillräckligt hög level? ⭐
Medel
Uppgift: Spelaren måste vara level 10 för att få gå in i en bossfight.

Instruktioner
Skapa variabeln level.

Ge den värdet 8.

Kontrollera om level är större än eller lika med 10.

Om villkoret stämmer ska du skriva "Du får gå in i bossfighten!".

Annars ska du skriva "Du måste levla upp först!".

```
python
# Sparar spelarens level
level = 8

# Kontrollerar om spelaren har tillräckligt hög level
if level >= 10:
    print("Du får gå in i bossfighten!")
else:
    print("Du måste levla upp först!")

```

# Du är en äventyrare som står framför två vägar. Du måste välja vilken väg du vill gå.

Instruktioner steg för steg
Skapa en variabel som heter val.

Använd input() för att fråga spelaren vilken väg den vill gå.

Ge spelaren två alternativ: 1 eller 2.

Skapa en if-sats som kontrollerar om spelaren väljer 1.

Om spelaren väljer 1 ska det stå "Du hittade en skatt!".

Använd elif för att kontrollera om spelaren väljer 2.

Om spelaren väljer 2 ska det stå "Du möter ett monster!".

Använd else om spelaren skriver något annat.

Färdig kod med kommentarer

```
python
# Frågar spelaren vilken väg den vill gå
val = input("Välj väg 1 eller 2: ")

# Kontrollerar om spelaren väljer väg 1
if val == "1":
    print("Du hittade en skatt!")

# Kontrollerar om spelaren väljer väg 2
elif val == "2":
    print("Du möter ett monster!")

# Om spelaren skriver något annat
else:
    print("Det valet finns inte!")

```

# Uppgift: Spelaren har 200 guldmynt och vill köpa ett vapen.

Instruktioner:

Skapa variabeln guld.

Ge den värdet 200.

Fråga spelaren vilket vapen den vill köpa.

Ett svärd kostar 100 guld.

En sköld kostar 150 guld.

Kontrollera om spelaren har råd.

Om spelaren har råd ska du dra av kostnaden från guld.

Skriv ut hur mycket guld spelaren har kvar.

Om spelaren inte har råd ska du skriva ett meddelande.

Exempel:

```

text
Du har 200 guld.
Vad vill du köpa? svärd
Du köpte ett svärd!
Du har 100 guld kvar.

```

