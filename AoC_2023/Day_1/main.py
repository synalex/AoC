def decodeString (num):
    if num == "zero" or num == "0":
        return 0
    elif num == "one" or num == "1":
        return 1
    elif num == "two" or num == "2":
        return 2
    elif num == "three" or num == "3":
        return 3
    elif num == "four" or num == "4":
        return 4
    elif num == "five" or num == "5":
        return 5
    elif num == "six" or num == "6":
        return 6
    elif num == "seven" or num == "7":
        return 7
    elif num == "eight" or num == "8":
        return 8
    elif num == "nine" or num == "9":
        return 9
    
def stringNumdecode (num):
    if len(num) == 1:
        if num in "zotfsen":
            return num
    if len(num) == 2:
        #["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
        if num in ["ze", "on", "tw", "th", "fo", "fi", "si", "se", "ei", "ni"]:
            return num
    if len(num) == 3:
        if num in ["zer", "one", "two", "thr", "fou", "fiv", "six", "sev", "eig", "nin"]:
            return num
        elif num[-2:] in ["on", "tw", "th", "fou", "fiv", "si", "se", "ei", "ni"]:
            return num[-2:]
    if len(num) == 4:
        if num in ["zero", "one", "two", "thre", "four", "five", "six", "seve", "eigh", "nine"]:
            return num
    if len(num) == 5:
        if num in ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
            return num
    return num[-1]
    

with open ("input.txt") as f:
    sum = 0
    for line in f:
        value = 0
        first = ""
        last = ""
        for char in line:
            if char in "0123456789":
                if first == "":
                    first = char
                else:
                    last = char
        if last in "":
            value = int(first + first)
        else:
            value = int(first + last)
        sum += value

print(sum)        

with open ("input.txt") as f:
    sum = 0
    i = 0
    for line in f:
        value = 0
        first = ""
        last = ""
        stringnum = ""
        i+=1
        if i == 300:
                print(f"test: {sum}")
        for char in line:
            stringnum = stringnum + char
            stringnum = stringNumdecode(stringnum)       
            line = line.strip()
            if char in "0123456789":   
                if first == "":
                    first = char
                    stringnum = stringnum[-1]
                else:
                    last = char
                    stringnum = stringnum[-1]
            elif stringnum in ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
                if first == "":
                    first = stringnum
                    stringnum = stringnum[-1]
                else:
                    last = stringnum
                    stringnum = stringnum[-1]
        if last in "":
            value = int(str(decodeString(first)) + str(decodeString(first)))
        else:
            value = int(str(decodeString(first)) + str(decodeString(last)))
        sum += value


print(sum)