import sys
string = input("Enter a string here...")

def palindrome(string):
    #If the given string is equal to its reverse option than its a Palindrome
    return string == string[::-1]


def near_Palindrome(string):
    #Loop through string and keep track of the occurencies of a given letter
    d = dict()
    for i in string:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    #Check for a value distinctive from the others, that has been appeard once
    odd_count = 0
    for k, v in d.items():
        if v%2 != 0 and odd_count== 0 :
            odd_count += 1
        elif v%2 !=0 and odd_count !=0:
            return False
    return True



pal = palindrome(string)
near_pal = near_Palindrome(string)

if len(string) <= 100000:
    if pal == True:
        print('Palindrome!')
    elif near_pal == True:
        print('Near Palindrome')
    else:
        print('Not Palindrome')

else:
    print("Woops! String length greater than 100000!")
    sys.exit(0)
