import sys

#Takes terminal argument as string
string1 = sys.argv[1]

def is_unique_string(string):
    #We will add our character bits into this variable and check it on every loop
    validator = 0
    #For every letter in our string
    for letter in range(len(string)):
        #get the letters corresponding bit
        bit = ord(string[letter]) - ord('a') + 1
        # if the bit is already set that means we have seen this char before
        if (validator & (1 << bit)) > 0:
            return False
        #we have not seen this bit before. Add a 1 the the position that corresponds to $bit
        validator |= (1 << bit)
    return True

if is_unique_string(string1):
    print("Unique: The string", string1, "is unique")
else:
    print("Not Unique: The string", string1, "is not unique")

