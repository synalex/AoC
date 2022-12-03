# i am noob with dicts be patient :(

from itertools import islice

elfs = {}
temp = 0
i = 1

with open('input.txt') as input_file:
    for line in input_file:
        current = line.strip() 
        if line not in ['\n', '\r\n']:
            temp+=int(current)
        else:       
            elfs[str(i)]=temp
            i+=1
            temp = 0

print(elfs)
max_keys = [key for key, value in elfs.items() if value == max(elfs.values())]

#find top calories
print("Elfs with most calories are:")
for key in max_keys:
    print(f"{key} : {elfs.get(key)}")

#find top 3 calories
elfs = sorted(elfs.items(), key=lambda x:x[1], reverse=True)
sorted_elfs = dict(elfs)
print(sorted_elfs)

top3 = 0
n= 3
plshelp = dict(islice(sorted_elfs.items(), n))
for item in plshelp.values():
    print(item)
    top3+=int(item)


print(f"The top 3 elfs have {top3} to carry")
