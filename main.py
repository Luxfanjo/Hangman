#Program "Debiloodborny"
import random
name = input("Podaj nick: ")
while len(name)==0:
    name = input("Podaj prawidłowy nick: ")
    
print(f'Witamy {name}!')
print(f'''Zasady gry:
        1) Baw się dobrze :)
        2) Możesz popełnić błąd 6 razy
        3) Litera którą wprowadzasz:
            I) Ma się składać z jednej litery
            II) Musi być literą
            III) Nie może być napisana caps lockiem/shiftem
      ''')
print("-------------------------------------------")

#Hasła
wordDic = ["obudowa", "ratusz", "banan", "procesor"]
#Program wybiera z haseł losowe hasło za pomocą funkcji .choice
randomWord = random.choice(wordDic)
#Wypisanie podpowiedzi
if randomWord == "obudowa":
    print("Budowa komputera")
elif randomWord == "ratusz":
    print("Reprezentacyjny budynek użyteczności publicznej")
elif randomWord =="banan":
    print("owoc")
elif randomWord == "procesor":
    print("Budowa komputera")
#Wypisanie linijek
for x in randomWord:
  print("_", end=" ")
#Wypisanie żyć
def print_hangman(wrong):
  if(wrong == 0):
    for i in range(0, 7):
        print("\n")    
    print(" ")
  elif(wrong == 1): 
    for i in range(0, 7):
        print("\n")    
    print("#")

  elif(wrong == 2):
    for i in range(0, 7):
        print("\n")    
    print("##")
      

  elif(wrong == 3):
    for i in range(0, 7):
        print("\n")    
    print("###")
      
  elif(wrong == 4):
    for i in range(0, 7):
        print("\n")    
    print("####")

  elif(wrong == 5):
    for i in range(0, 7):
        print("\n")    
    print("#####")
  elif(wrong == 6):
    for i in range(0, 7):
        print("\n")    
    print("######")
#Licznik
def printWord(guessedLetters):
  counter=0
  rightLetters=0
  for char in randomWord:
    if(char in guessedLetters):
      print(randomWord[counter], end=" ")
      rightLetters+=1
    else:
      print(" ", end=" ")
    counter+=1
  return rightLetters

def printLines():
  print("\r")
  for char in randomWord:
      #Tak zwany overline character \u203E
    print("\u203E", end=" ")


lenWordGuessed = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 6 and current_letters_right != lenWordGuessed):
#Litery które użytkownik już podał
  print("\n Użyte litery: ")
  for letter in current_letters_guessed:
    print(letter, end=" ")
#Pobranie litery od użytkownika
  letterGuessed = input("\n Zgadnij literę: ")
  #Sprawdzenie czy input jest zgodny z zasadami i ponowne pobranie litery od użytkownika
  while len(letterGuessed)!=1 or letterGuessed.isupper() == True or letterGuessed.isdigit() == True:
    print( f'''
          Litera którą wprowadzasz:
            I) Ma się składać z jednej litery
            II) Musi być literą
            III) Nie może być napisana caps lockie/shiftem''')
    letterGuessed = input("\n Wpisz literę zgodnie z zasadami gry: ")

#Dobrze
  if(randomWord[current_guess_index] == letterGuessed):
    print_hangman(amount_of_times_wrong)
    current_guess_index+=1
    current_letters_guessed.append(letterGuessed)
    current_letters_right = printWord(current_letters_guessed)
    printLines()
#Źle
  else:
    amount_of_times_wrong+=1
    current_letters_guessed.append(letterGuessed)
    print_hangman(amount_of_times_wrong)
    current_letters_right = printWord(current_letters_guessed)
    printLines()
#Przegrał
if amount_of_times_wrong==6: 
    print(f'Przegrałeś! Prawidłowe hasło to: {randomWord}')
#Wygrał
else:
    print(f'Brawo! Dziękujemy za grę {name}')

#Kamil Kaczmarek 3Pr
