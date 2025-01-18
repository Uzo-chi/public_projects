import re

passwordRegex = re.compile(r'''(
    ([a-zA-Z0-9]){8,}
    )''', re.VERBOSE)

upperRegex = re.compile(r'[A-Z]')
lowerRegex = re.compile(r'[a-z]')
numRegex = re.compile(r'[0-9]')

def passwordChecker(password):
    pass1 = upperRegex.search(password)
    pass2 = lowerRegex.search(password)
    pass3 = numRegex.search(password)
    
    if pass1 != None and pass2 != None and pass3 != None:
        final_pass = passwordRegex.search(password)
        if final_pass != None:
            print("\nYour password is very strong!")
        else:
            print("\nYour password isn't very strong (less than 8 characters)")
    else:
        print("\nYour password isn't very strong because:")
        if pass1 == None:
            print("- it has no uppercase letters.")
        if pass2 == None:
            print("- it has no lowercase letters")
        if pass3 == None:
            print("- it has no numbers")
            
user = input("Enter your password: ")
passwordChecker(user)