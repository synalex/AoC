def find_range(pair1,pair2):
    pair1 = list(map(int, pair1)) 
    pair2 = list(map(int, pair2)) 

    if pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:
        return True 
    elif pair1[0] <= pair2[0] and pair1[1] >= pair2[1]:
        return True
    else:
        return False

def find_range2(pair1,pair2):
    pair1 = list(map(int, pair1)) 
    pair2 = list(map(int, pair2)) 

    if pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:
        return True 
    elif pair1[0] <= pair2[0] and pair1[1] >= pair2[1]:
        return True
    elif pair1[0] >= pair2[0] and pair1[0] <= pair2[1]:
        return True
    elif pair1[0] <= pair2[0] and pair1[1] >= pair2[0]:
        return True
    elif pair1[1] >= pair2[0] and pair1[1] <= pair2[1]:
        return True
    elif pair1[1] >= pair2[1] and pair1[0] <= pair2[1]:
        return True
    else:
        return False

n=0
with open('input.txt') as input_file:
    for line in input_file:
        current = line.strip().split(",")
        if find_range(current[0].split("-"), current[1].split("-")):
            n+=1
        else:
            pass

print(f"In {n} assignment pairs does one range fully contain the other!")

n=0
with open('input.txt') as input_file:
    for line in input_file:
        current = line.strip().split(",")
        if find_range2(current[0].split("-"), current[1].split("-")):
            n+=1
        else:
            pass

print(f"In {n} assignment pairs does have overall overlaping values!")
