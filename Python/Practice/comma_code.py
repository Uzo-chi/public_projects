def list_to_string(list):
    """Take a list and return a string of comma seperated text."""
    
    text = ""
    
    for i in range(len(list)):
        if i == 0:
            text = f"{list[i]}, "
        elif i == (len(list) - 1):
            text += f"and {list[i]}"
        else:
            text += f"{list[i]}, "
            
    return text

spam = ['apples', 'bananas', 'tofu', 'cats', 'pillows', 'friends', 'food']
result = list_to_string(spam)

print(result)