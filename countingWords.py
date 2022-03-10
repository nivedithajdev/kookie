introString=input("enterString:")
characterCount=0
wordCount=1
for i in introString:
    characterCount=characterCount+1
    if(i==""):
        wordCount=wordCount+1
print("number of word in string")
print(wordCount)
print("number of character")
print(characterCount)


