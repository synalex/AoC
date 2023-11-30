# if string is in more than one index
def treat_input(input):
   with open(input) as file:
     input = file.readlines()
     signal = ""
     for x in input:
       signal += x
     return signal


# index+1 cuz we need to look at the marker not on the n-th last char of the set
def find_marker(signal, n):
  check = ""
  for index, char in enumerate(signal):
    if char not in check:
       check+=char
       if len(check) == n:
          check += char
          return index+1
       else:
          pass
    else:
      check=char
  return(":/")  


print("Task 1: ")
print(find_marker(treat_input("input.txt"),4))

print("\n")
print("Task 2: ")
print(find_marker(treat_input("input.txt"),14))





