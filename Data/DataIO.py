namesBelow5 = []

with open('lastnames.txt','r') as fil:
    out = fil.read().split('\n')

for i in out:
    if len(i) > 5: # You change as you please
        namesBelow5.append(i)

print(namesBelow5)