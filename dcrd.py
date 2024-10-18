import random
a=['heart','diamond','spade','club']
b=['ace','1','2','3','4','5','6','7','8','9','j','k','q']
deck=[]
for i in a:
    for j in b:
        deck.append(i+j)
random.shuffle(deck)
print(deck)