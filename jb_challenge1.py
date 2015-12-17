#!/usr/bin/python

file = open("story.txt", "r")
file_contents = file.read()

#Count number of words using split()
def get_words(story):
    words = len(story.split())
    return words

#Count number of sentences by counting terminal punctuation(?,!,.)
def get_sentences(story):
    x = story.count('.')
    y = story.count('?')
    z = story.count('!')
    sentences = x + y + z
    return sentences

def get_paragraphs(story):
    paragraphs = story.split("\n\n")
    number_of_paragraphs = len(paragraphs)
    return number_of_paragraphs

def get_unique_count(story):
    words = []
    wordcount = 0
    for word in story.split():
        if word not in words:
            wordcount += 1
            words.append(word)
        else:
            pass 
    return wordcount

print "Total Unique Words: {}".format(get_unique_count(file_contents))
print "Total Word Count: {}".format(get_words(file_contents))
print "Paragraphs: {}".format(get_paragraphs(file_contents))
print "Sentences: {}".format(get_sentences(file_contents))
