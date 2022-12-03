def is_member(List, key):
 
    for i in range(0, len(List)):
        if key == List[i]:
            return True
    return False
 
def overlap(List1 , List2):
 
    for key in List1:
        if is_member( List2, key ):
            return key
 
    return False

def find_duplicate(rucksack):
    rucksack
    firstpart, secondpart = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    return prio.get(overlap(firstpart, secondpart))

def find_duplicate2(line1, line2, line3):
    s1 = set(line1)
    s1 = s1.intersection(set(line2))
    s1 = s1.intersection(set(line3))
    s1 = list(s1)
    return prio.get(s1[0])


# Initialize alphabet dict
# only learned about ascii in py afterwards
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet += [letter.upper() for letter in alphabet]
values = [i for i in range(1,53)]
prio = { k:v for (k,v) in zip(alphabet, values)}
print(prio)

total = 0
i=0
with open('input.txt') as input_file:
    for line in input_file:
        total+=find_duplicate(line.strip())

print(f"sum of the priorities is {total}!")

total = 0
i = 0
temp = ""
temp2 = ""
temp3 = ""
with open('input.txt') as input_file:
    for line in input_file:
        if i == 3:
            total+=find_duplicate2(temp, temp2, temp3)
            i=1
            print(temp)
            print(temp2)
            print(temp3)
            temp = line.strip()
            temp2 = ""
            temp3 = ""
        else:
            if temp == "":
                temp = line.strip()
            elif temp2 == "":
                temp2 = line.strip()
            elif temp3 == "":
                temp3 = line.strip()
            i+=1
    if i == 3:
            total+=find_duplicate2(temp, temp2, temp3)
            i=1
            print(temp)
            print(temp2)
            print(temp3)
            temp = line.strip()
            temp2 = ""
            temp3 = ""


print(f"sum of the priorities is {total} for 3 lines!")
        