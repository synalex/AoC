##could have made rock= a, x etc. but lazy

# A = 1p, B =2p, C=3p
def calc(me, opp):
    if me == "X": 
        if opp == "A":
            return 4
        elif opp == "B":
            return 1
        elif opp == "C":
            return 7
    elif me =="Y":
        if opp == "A":
            return 8
        elif opp == "B":
            return 5
        elif opp == "C":
            return 2
    elif me =="Z":
        if opp == "A":
            return 3
        elif opp == "B":
            return 9
        elif opp == "C":
            return 6

#X=L, Y=D, Z=W
def calc2(me, opp):
    if me == "X": 
        if opp == "A":
            return calc("Z","A")
        elif opp == "B":
            return calc("X","B")
        elif opp == "C":
            return calc("Y","C")
    elif me =="Y":
        if opp == "A":
            return calc("X","A")
        elif opp == "B":
            return calc("Y","B")
        elif opp == "C":
            return calc("Z","C")
    elif me =="Z":
        if opp == "A":
            return calc("Y","A")
        elif opp == "B":
            return calc("Z","B")
        elif opp == "C":
            return calc("X","C")

total = 0
with open('input.txt') as input_file:
    for line in input_file:
        total+=calc(line[2], line[0])

print(f"I 'd have {total} amount of points if I knew the best answer!")

total = 0
with open('input.txt') as input_file:
    for line in input_file:
        total+=calc2(line[2], line[0])

print(f"I 'd have {total} amount of points if I knew the best outcome!")
    

    

