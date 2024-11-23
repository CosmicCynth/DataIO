import requests
from requests import Request

loripsum = requests.get('https://loripsum.net/api/plaintext/10/long')
print(loripsum.text)

print("FILTERED TEXT")

AP = loripsum.text.count(".")
AP = AP+loripsum.text.count("?")
AP = AP+loripsum.text.count("!")
WordList = loripsum.text.split()
symbols_to_remove = ",@#!.?;:-"
UpdatedWordList = [item.translate(str.maketrans('', '', symbols_to_remove)) for item in WordList]
Longwords = 0
Words = len(UpdatedWordList)
print(UpdatedWordList)

for i in UpdatedWordList:
    if len(i) > 6:
        Longwords += 1



print("Sætninger: " +str(AP), "Antal ord: " + str(Words), "Lange ord: " + str(Longwords))


LixTal = (Words/AP)+(Longwords*100/Words)
Lixtal = round(LixTal)

print("Lix tal er " + str(Lixtal))

def difficulty():
    Difficulty = ""
    if Lixtal <= 24:
        Difficulty = "Let"
    if Lixtal > 24 < 35:
        Difficulty = "Let for øvede læsere"
    if Lixtal > 34 < 45:
        Difficulty = "Middel"
    if Lixtal > 44 < 55:
        Difficulty = "Svær"
    if Lixtal > 55:
        Difficulty = "Meget svær"
    return(Difficulty)

print("Sværhedsgrad: " + str(difficulty()))

