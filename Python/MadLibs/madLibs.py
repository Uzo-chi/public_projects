import re

wordRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

textFile = open("test1.txt")
textContents = textFile.read()

wordClasses = wordRegex.findall(textContents)

for word in wordClasses:
    choice = input("\nEnter a(n) %s: " %(word.lower()))
    textContents = wordRegex.sub(choice,textContents,1)
    
outputFile = open("output.txt", 'w')

outputFile.write(textContents)
outputFile.close()
textFile.close()