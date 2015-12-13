#!/usr/bin/python

file = open("story.txt", "r+")

#words = 0
#unique = 0
#paragraphs = 0
#sentences = 0


#def get_words():
#for word in file.read().split():
words = file.read().split()
number_of_words = len(words)
print "Words: {words}".format(words=number_of_words)

#def get_sentences():
sentences = file.read().split('. ')
number_of_sentences = len(sentences)
print "Sentences: {sentences}".format(sentences=number_of_sentences)


#def get_paragraphs():
paragraphs = file.read().split("\n\n")
number_of_paragraphs = len(paragraphs)
print "Paragraphs: {paragraphs}".format(paragraphs=number_of_paragraphs)

print "Unique words and their counts: \n"

#def get_unique_count():
wordcount = {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k, v in wordcount.items():
    print k, v
