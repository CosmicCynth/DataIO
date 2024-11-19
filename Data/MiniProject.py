import requests
from requests import Request

loripsum = requests.get('https://loripsum.net/api/plaintext/10/long')
print(loripsum.text)


AP = loripsum.text.count(".")
WordList = loripsum.text.split()
Words = len(WordList)
Longwords = 0


for i in WordList:
    if len(i) > 6:
        Longwords += 1

print("Punktumer: " +str(AP), "Antal ord: " + str(Words), "Lange ord: " + str(Longwords))


LixTal = Words/AP+Longwords*100/Words
Lixtal = round(LixTal)

print("Lix tal er " + str(Lixtal))


