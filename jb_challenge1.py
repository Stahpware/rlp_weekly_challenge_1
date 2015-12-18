#!/usr/bin/python

file = open("story.txt", "r")
file_contents = file.read()


def get_words(story):
    '''Count number of words using split()'''
    words = len(story.split())
    return words


def get_sentences(story):
    '''Count number of sentences by counting terminal punctuation(?,!,.)'''
    x = story.count('.')
    y = story.count('?')
    z = story.count('!')
    sentences = x + y + z
    return sentences


def get_paragraphs(story):
    '''Count number of paragraphs by splitting on 2 newlines.'''
    paragraphs = story.split("\n\n")
    number_of_paragraphs = len(paragraphs)
    return number_of_paragraphs


def get_unique_count(story):
    '''Grab Unique words and count how many times they are used.'''
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
