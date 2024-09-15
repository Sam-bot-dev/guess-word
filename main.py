import random
turns=12
guesses=''
print("Welcome to the word guessing game!")
name=input("What is your name?\n")
print("Good luck",name,"boi\n")
print("chooce your type of word \n[animals, fruits, places,holidays,music_instruments] ")
num=int(input("1 For Animals\n2 For Fruits\n3 For Places\n4 For Holidays\n5 For Music Instruments\n"))
if (num==1):
  print("you have chosen animals")
  animals=["Dog","Cow",'Cat','Horse',
'Donkey','Tiger','Lion','Panther'
,'Leopard',	'Cheetah']
  animal=random.choice(animals)
  while turns>0:
    failed=0
    for char in animal:
      if char in guesses:
        print(char, end=" ")
      else:
        print("_")
        failed += 1
      if failed == 0:
        print("You Win")
        print("The word is: ", animal)
        break
      print()
      guess = input("guess a character:")

      guesses += guess

      if guess not in animal:

          turns -= 1
          print("Wrong")
          print("You have", + turns, 'more guesses')

          if turns == 0:
              print("You Loose")
    
    
  print(animal)
elif (num==2):
  print("you have chosen fruits")
  fruits=["Banana","Apple" ,"Strawberry","Avocado","Pineapple", "Watermelon","Mango","Kiwi","Orange","Berry","Blueberry"]
  fruit=random.choice(fruits)
  while turns>0:
    failed=0
    for char in fruit:
      if char in guesses:
        print(char, end=" ")
      else:
        print("_")
        failed += 1
      if failed == 0:
        print("You Win")
        print("The word is: ", fruit)
        break
      print()
      guess = input("guess a character:")

      guesses += guess

      if guess not in fruit:

          turns -= 1
          print("Wrong")
          print("You have", + turns, 'more guesses')

          if turns == 0:
              print("You Loose")
  
  print(fruit)
elif (num==3):
  print("you have chosen places")
  places=["Paris","London","New York","Tokyo","Dubai","Moscow","Rome","Beijing","Mumbai","Mexico City","Cairo","Rio de Janeiro","Sydney","Toronto","Melbourne","Auckland","Perth","Seoul","Bangkok","Buenos Aires","Lima","Bogota","Havana","Jakarta","Kyoto","Madrid","Mexico City","Cairo","Rio de Janeiro","Sydney","Toronto","Melbourne","Auckland","Perth","Seoul","Bangkok","Buenos Aires","Lima","Bogota","Havana","Jakarta","Kyoto","Madrid","Mexico City","Cairo","Rio de Janeiro","Sydney","Toronto","Melbourne","Auckland","Perth","Seoul","Bangkok","Buenos Aires","Lima","Bogota","Havana"]

  place=random.choice(places)
  while turns>0:
    failed=0
    for char in place:
      if char in guesses:
        print(char, end=" ")
      else:
        print("_")
        failed += 1
      if failed == 0:
        print("You Win")
        print("The word is: ", place)
        break
      print()
      guess = input("guess a character:")

      guesses += guess

      if guess not in place:

          turns -= 1
          print("Wrong")
          print("You have", + turns, 'more guesses')

          if turns == 0:
              print("You Loose")
  print(place)
elif (num==4):
  print("you have chosen holidays")
  holidays=["Christmas","Thanksgiving","Halloween","New Years","Valentines Day","Easter","St. Patricks Day","Independence Day","Labor Day","Hanukkah","Rosh Hashanah","Memorial Day","Veterans Day","Fathers Day","Mothers Day","4th of July","Halloween","Thanksgiving","Christmas","Easter","St. Patricks Day","Independence Day","Labor Day","Hanukkah","Rosh Hashanah","Memorial Day","Veterans Day","Fathers Day","Mothers Day","4th of July"]
  holiday=random.choice(holidays)
  while turns>0:
    failed=0
    for char in holiday:
      if char in guesses:
        print(char, end=" ")
      else:
        print("_")
        failed += 1
      if failed == 0:
        print("You Win")
        print("The word is: ", holiday)
        break
      print()
      guess = input("guess a character:")

      guesses += guess

      if guess not in holiday:

          turns -= 1
          print("Wrong")
          print("You have", + turns, 'more guesses')

          if turns == 0:
              print("You Loose")
  print(holiday)
elif (num==5):
  print("you have chosen music instruments")
  music_instruments=[ "Guitar","Piano","Drums","Flute","Violin","Trumpet","Saxophone","Clarinet","Trombone","Bassoon","Harp","Tuba","Xylophone"]
  music_instrument=random.choice(music_instruments)
  while turns>0:
    failed=0
    for char in music_instrument:
      if char in guesses:
        print(char, end=" ")
      else:
        print("_")
        failed += 1
      if failed == 0:
        print("You Win")
        print("The word is: ", music_instrument)
        break
      print()
      guess = input("guess a character:")

      guesses += guess

      if guess not in music_instrument:

          turns -= 1
          print("Wrong")
          print("You have", + turns, 'more guesses')

          if turns == 0:
              print("You Loose")
  print(music_instrument)
