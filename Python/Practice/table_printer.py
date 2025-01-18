"""
Python code to display a list of lists in order of rows and columns
with the columns right-justified
"""

def printTable(strings):
    # Initialize the colWidths list to be equal to the
    # number of embedded lists in strings
    
    colWidths = [0] * len(strings)
    
    # Initialize the totalMax variable
    
    totalMax = 0
    
    # Loop through the strings list first and initialize
    # the max variable
    for i in range(len(strings)):
        max = len(strings[i][0])
        
        # Assuming that all embedded lists are the same length,
        # find the string with the highest number of words and set
        # the corresponding position of colWidths to the value of the
        # string's length
        
        for j in range(len(strings[i])):
            if len(strings[i][j]) > max:
                max = len(strings[i][j])
        colWidths[i] = max
        
    for num in colWidths:
        if num > totalMax:
            totalMax = num
    
    # Assume that all lists embedded in strings have equal length
    # then loop through them to display output in rows and columns
    
    for a in range(len(strings[0])):
        for b in range(len(strings)):
            print(strings[b][a].rjust(totalMax),end='')
        print("")
            
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# Call function printTable
printTable(tableData)