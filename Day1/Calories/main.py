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

print("Elfs with most calories are:")
for key in max_keys:
    print(f"{key} : {elfs.get(key)}")
