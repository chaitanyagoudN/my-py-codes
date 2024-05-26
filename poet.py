from textblob import TextBlob
#from nltk.corpus import stopwords
#import nltk
#nltk.download('stopwords')

#stops= stopwords.words('english')
#POS
def pos_count(tags,part_of_speech):
    instances = 0
    for tag in tags:
        if tag[1] in part_of_speech:
            instances +=1
    return instances

text = ""
with open("/Users/vamshrihari/Desktop/ship1.txt")as poems:
    lines=poems.readlines()
    for line in lines:
        text += " " + line.rstrip()
texts={}


the_blob = TextBlob(text)

#1
print(len(the_blob.sentences))
#2
print(len(the_blob.words))
print(pos_count(the_blob.tags,["JJ","NNP"]))
print(the_blob.tags)

#print(the_blob.word)