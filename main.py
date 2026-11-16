

def example():
  
  # Ber användaren skriva ett heltal och sparar det i variabeln antal
  antal = int(input("Skriv ett heltal "))

# Skapar variabeln raknare och ger den startvärdet 1
  raknare = 1

# Så länge raknare är mindre än eller lika med antal körs loopen
  while raknare <= antal:

    # Multiplicerar raknare med 7 och skriver ut resultatet
      print(raknare * 7)

    # Ökar raknare med 1 för varje varv i loopen
      raknare = raknare + 1

  
example()


def exercise_one():
  # Skapa ett program som räknar ned från 10 till 1

  # 1. Skapa en variabel som heter raknare med värde 10.

  # 2. Skapa en while-loop.

  # 3. Skriv villkoret så att loopen fortsätter så länge raknare är större än eller lika med 1. 

  # 4. Skriv ut värdet på raknare

  # 5. Minska värdet på raknare med 1 efter varje varv.

  # 6. Testa att köra programmet! 

exercise_one()

def exercise_two():
  #  Spelaren börjar med 100 HP (health points). Varje gång spelaren tar skada förlorar den 20 HP.

  # 1. Skapa en variabel som heter health_points med värdet 100

  # 2. Skapa en while-loop.

  # 3. Loopen ska fortsätta så länge spelarens health_points är större än 0

  # 4. Skriv ut spelarens aktuella hälsa.

  # 5. Minska hälsan (healt_points) med 20 efter varje varv.

  # 6. När hälsan når 0 eller lägre ska du skriva ut "Game Over!". (Utanför while loopen)
