import re

def regexStripper(string, scrap=""):
    if scrap == "":
        rstripRegex = re.compile(r'^(\w.*\w)(\s)+$')
        lstripRegex = re.compile(r'^(\s)+(\w.*\w)$')
        stripRegex = re.compile(r'^(\s)+(\w.*\w)(\s)+$')
        
        if len(stripRegex.findall(string)) > 0:
            trim = stripRegex.findall(string)
            return trim[0][1]
        elif len(lstripRegex.findall(string)) > 0:
            trim = lstripRegex.findall(string)
            return trim[0][1]
        elif len(rstripRegex.findall(string)) > 0:
            trim = rstripRegex.findall(string)
            return trim[0][0]
        else:
            return string
    else:
        item = r'[' + re.escape(scrap) + r']'
        scrapRegex = re.compile(item)
        
        return scrapRegex.sub("", string)
        
        
user = input("Enter a string to be stripped: ")
print("\nWhat would you like to strip:\n")
print("- Enter 1 for whitespace\t- Enter 2 for something of your choice\n")
choice = input("Your choice: ")

if choice == '1':
    print(f"\nYour string before: '{user}'")
    print(f"\nYour string after: '{regexStripper(user)}'\n")
elif choice == '2':
    print(f"\nYour string: '{user}'")
    scrap = input("What would you like to remove from your string: ")
    print(f"\nYour string after: '{regexStripper(user, scrap)}'")
else:
    print("\nWrong choice!")
    
print("\nDone!")    