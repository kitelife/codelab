import os

wordInfo={}

for fileName in os.listdir('D:\\test'):
    print fileName
    fileHandle=open('D:\\test\\'+fileName)
    content=fileHandle.readlines()
    for line in content:
        words=line.split(' ')
        for word in words:
            word=word.replace('\n','')
            word=word.replace(',','')
            word=word.replace('(','')
            word=word.replace(')','')
            word=word.replace('"','')
 
            i=0
            for be in wordInfo:
                if word==be:
                    i=i+1
            if i!=0:
                for be in wordInfo:
                    if word==be:
                        wordInfo[be]=wordInfo[be]+1
                        break
            else:
                wordInfo[word]=1
 
    for word in wordInfo:
        print word,':',wordInfo[word]