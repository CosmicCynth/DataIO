#with open('beerbottlesong.txt','w') as fil:
BeerBottles = 99

while BeerBottles > 0:
    print(str(BeerBottles) + " Bottles of beer on the wall " + str(BeerBottles) + " Bottles of beer. Take one down and pass it around, ")
    BeerBottles = BeerBottles - 1
    print(str(BeerBottles) + " Bottles of beer on the wall.")
