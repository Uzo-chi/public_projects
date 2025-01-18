import os, re

directory = input("Enter the directory to search: ")
directory = re.escape(directory)

if os.path.isdir(directory) == False:
    print("Directory does not exist")
else:
    textFiles = []
    
    textRegex = re.compile(r'\.txt$')
    
    userInput = input("Enter your regex pattern: ")
    userInput = re.escape(userInput)
    userRegex = re.compile(userInput)
    
    print("\n-----Scanning through directory-----")
    
    fileList = os.listdir(directory)
    
    for f in fileList:
        if textRegex.search(f) != None:
            textFiles.append(f)
    if len(textFiles) > 0:
        for text in textFiles:
            filePath = os.path.join(directory, text)
            file = open(filePath)
            fileContents = file.readlines()
            
            print(f"--------- {text} ---------")
            
            for content in fileContents:
                if len(userRegex.findall(content)) > 0:
                    print(content)
            
            file.close()