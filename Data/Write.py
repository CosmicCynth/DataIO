

BeerBottles = 99
Song = ""

while BeerBottles > 0:

    if BeerBottles == 1:
        bottle_word = "Bottle"
    else:
        bottle_word = "Bottles"

    Song+=(str(BeerBottles)+ " " + bottle_word + " of beer on the wall " + str(BeerBottles)+" " + bottle_word + " of beer. Take one down and pass it around, ")
    BeerBottles = BeerBottles - 1

    if BeerBottles == 1:
        bottle_word = "Bottle"
    else:
        bottle_word = "Bottles"

    Song+=(str(BeerBottles) + " " + bottle_word + " of beer on the wall.\n")

with open('beerbottlesong.txt','w') as fil:
    fil.write(Song)