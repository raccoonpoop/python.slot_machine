import random
import os
os.system('cls' if os.name == 'nt' else 'clear')
gamble= ['🍇','🍉','🍊','🍓','🫐','🍒','🔔','7']
print("**************")
print("*Slot_Machine*")
print("**************")

gamble1=[random.choice(gamble) for _ in range(3)]
print(gamble1)
print("**************")
