import pandas

mijndata= pandas.read_csv("Pokemon.csv")

#print(mijndata)
#print("csv")
# reference guide (docs documentation api)

#print(mijndata.columns)
#print(mijndata.items)

#print (mijndata["Name"])
name = input ("zoek je favoriete pokemon ")
gevonden = False
#for each loop
for mijnpokemon in mijndata ["Name"]:
    #print (mijnpokemon)
    if name == mijnpokemon:
        gevonden = True
        #print ("Yes, gevonden!") 
    #if name != mijnpokemon:
       #print ("Deze pokemon is niet gevonden...")
print (name)
if gevonden:
    print("Ja, gevonden! ")
else:
    print("Niet gevonden")
# Zoek je favoriete pokemon



# Hoeveel en welke pokemon zijn sterker dan 80

# Welke type 1 heeft gemiddeld de meeste defence

