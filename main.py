import random
turns=12
Guesses=''
print("Welcome to the word guessing game!")
name=input("What is your name?\n")
print("Good luck",name,"boi\n")
print("chooce your type of word \n[animals, fruits, places,holidays,music_instruments] ")
num=int(input("1 For Animals\n2 For Fruits\n3 For Places\n4 For Holidays\n5 For Music Instruments\n"))
if (num==1):
  print("you have chosen animals")
  animals=["lion","tiger","dog","cat","wolf","bear","horse","cow","pig","sheep","goat","chicken","duck","donkey","rabbit","mouse","fox","deer","elephant","monkey","giraffe","zebra","kangaroo","koala","penguin","dolphin","shark","whale","octopus","squid","jellyfish","turtle","snake","frog","spider","ant","bee","butterfly","ladybug","dragonfly","caterpillar","mantis","grasshopper","cricket","chameleon","leopard","cheetah","rhinoceros","hippopotamus","ostrich","eagle","hawk","peacock","parrot","swan","flamingo","penguin","dove","swallow","crow","owl","pigeon","pelican","parrot","toucan","flamingo","ostrich","eagle","hawk","peacock"]
  animal=random.choice(animals)
  print(animal)
elif (num==2):
  print("you have chosen fruits")
  fruits=["Banana","Apple" ,"Strawberry","Avocado","Pineapple", "Watermelon","Mango","Kiwi","Orange","Berry","Blueberry"]
  fruit=random.choice(fruits)
  print(fruit)
elif (num==3):
  print("you have chosen places")
  places=["Paris","London","New York","Tokyo","Dubai","Moscow","Rome","Beijing","Mumbai","Mexico City","Cairo","Rio de Janeiro","Sydney","Toronto","Melbourne","Auckland","Perth","Seoul","Bangkok","Buenos Aires","Lima","Bogota","Havana","Jakarta","Kyoto","Madrid","Mexico City","Cairo","Rio de Janeiro","Sydney","Toronto","Melbourne","Auckland","Perth","Seoul","Bangkok","Buenos Aires","Lima","Bogota","Havana","Jakarta","Kyoto","Madrid","Mexico City","Cairo","Rio de Janeiro","Sydney","Toronto","Melbourne","Auckland","Perth","Seoul","Bangkok","Buenos Aires","Lima","Bogota","Havana"]

  place=random.choice(places)
  print(place)
elif (num==4):
  print("you have chosen holidays")
  holidays=["Christmas","Thanksgiving","Halloween","New Years","Valentines Day","Easter","St. Patricks Day","Independence Day","Labor Day","Hanukkah","Rosh Hashanah","Memorial Day","Veterans Day","Fathers Day","Mothers Day","4th of July","Halloween","Thanksgiving","Christmas","Easter","St. Patricks Day","Independence Day","Labor Day","Hanukkah","Rosh Hashanah","Memorial Day","Veterans Day","Fathers Day","Mothers Day","4th of July"]
  holiday=random.choice(holidays)
  print(holiday)
elif (num==5):
  print("you have chosen music instruments")
  music_instruments=[ "Guitar","Piano","Drums","Flute","Violin","Trumpet","Saxophone","Clarinet","Trombone","Bassoon","Harp","Tuba","Xylophone"]
  music_instrument=random.choice(music_instruments)
  print(music_instrument)
