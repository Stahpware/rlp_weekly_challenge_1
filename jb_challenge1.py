#!/usr/bin/python
import argparse

file = open("story.txt", "r")
file_contents = file.read()

stats = {}


def main():
    parser = argparse.ArgumentParser(description='Processes file statistics.')
    parser.add_argument('-f', '--story-file', dest='story_file', default='story.txt', help='Story file that you want the stats for.')
    args = parser.parse_args()
    print stats
    #for result in log_scan(args.log_directory, args.log_file_format, args.log_date, args.log_date_format):
        #print result


def get_words(story):
    '''Count number of words using split()'''
    words = len(story.split())
    stats["Words"] += 1
    print stats["Words"]
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

#print "Total Unique Words: {}".format(get_unique_count(file_contents))
#print "Total Word Count: {}".format(get_words(file_contents))
#print "Paragraphs: {}".format(get_paragraphs(file_contents))
#print "Sentences: {}".format(get_sentences(file_contents))


if __name__ == "__main__":
    main()
