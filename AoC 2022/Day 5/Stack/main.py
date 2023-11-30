import string
import copy

# rearrange with original order
def rearrange2 (n, old, new, stack):
        old, new = old-1, new-1
        values = []
        for _ in range (n):
                values.append(stack[old].pop())
        for _ in range (n):
                stack[new].append(values.pop())
        return stack

# lifo rearrangement
def rearrange (n, old, new, stack):
        old, new = old-1, new-1
        for _ in range (n):
                stack[new].append(stack[old].pop())
        return stack
        



with open("input.txt") as file:

    # declaring variables we need later:
    position = 0
    current = 8
    stacks = []
    alphabet = string.ascii_uppercase

    #read data 
    stack_data, commands= file.read().strip().split('\n\n')

    #create pattern like this for example: [["x", "y"], ["x"]]
    stack_data = stack_data[::-1]
    stack_data = stack_data.strip()
    stack_data= stack_data.split("]", 1)
    stack_data[1] = stack_data[1].split("\n")
    stack_data[1][0] = "]" + stack_data[1][0]
    
    # figure out how many stacks
    nums = [x for x in range(1,10)]  
    for char in stack_data[0]:
        try:
            if int(char) in nums:
               stacks.append([])
        except ValueError:
            pass      
    
    
    # every 4 steps there is either a letter or a whitespace. if letter add to stack if whitespace skip
    # current keeps track of current stack
    # position keeps track of the n-th new element in a stack
    for position in range(len(stack_data[1])):
        current = 8
        for char in range(1,len(stack_data[1][position]),4):
                if stack_data[1][position][char] in alphabet:
                        stacks[current].append(stack_data[1][position][char])
                        current-=1
                elif stack_data[1][position][char] in [" "]:
                        current-=1
                elif stack_data[1][position][char] in ["["]:
                        current = 8

    # commands
    # begin with list[1] 1:
    # with 2-steps
    commands= [ [int(x) for x in line.split(" ")[1::2] ] for line in commands.split('\n') ]
   
    # copy stack so we can mess around with
    stacks_copy = copy.deepcopy(stacks)
    for move in commands:
        stacks_copy= rearrange(*move, stacks_copy)

    # get 1st element of each stack
    task1 = ""
    for n in range(len(stacks_copy)):
        task1 = task1 + stacks_copy[n].pop()
    
    print(f"After the rearrangement procedure completes,  on top of each stack end up: {task1}")

    stacks_copy = copy.deepcopy(stacks)
    print(stacks_copy) 
    for move in commands:
        stacks_copy= rearrange2(*move, stacks_copy)
    
    # get 1st element of each stack
    task2 = ""
    for n in range(len(stacks_copy)):
        task2 = task2 + stacks_copy[n].pop()
    
    print(f"After the rearrangement without changing the original order procedure completes,  on top of each stack end up: {task2}")
