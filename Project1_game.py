import random
def gameWin(comp,you):

# if two values are equal
    if comp == you:
        return None

# if comp choses S that is Snake 
    elif comp == 'S':   
        if you == 'G':
            return True
        elif you == 'W':
            return False

 # if comp choses G that is Gun
    elif comp == 'G':
        if you == 'S':
            return False
        elif you == 'W':
            return True

# if comp choses W that is water
    elif comp == 'W':
        if you == 'G':
            return False
        elif you == 'S':
            return True                            

print ("Comp Turn: Snake(S), Water (W), Gun(G)?")
randNo = random.randint(1,3)
if randNo ==1:
    comp = 'S'
elif randNo ==2:
    comp = 'W'
elif randNo ==3:
    comp = 'G'

you = input("Your turn: Snake(S), Water (W), Gun(G)?")
a = gameWin(comp, you)

print(f"Comp chose {comp}")
print(f"you chose {you}")

if a == None:
    print ("It's a Tie!")
elif a == True:
    print ("You won!")
else:
    print ("You lost!")
    

