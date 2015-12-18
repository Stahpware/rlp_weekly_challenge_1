#!/usr/bin/env python
import argparse
stats = {}


def main():
    parser = argparse.ArgumentParser(description='Processes file statistics.')
    parser.add_argument('-f', '--story_file', dest='story',
                        default='story.txt',
                        help='Story file that you want the stats for.')
    args = parser.parse_args()
    with open(args.story, "r") as file:
        file_contents = file.read()
    get_words(file_contents)
    get_sentences(file_contents)
    get_paragraphs(file_contents)
    get_unique_count(file_contents)
    for key, value in stats.items():
        print "{}: {}".format(key, value)


def get_words(story):
    '''Count number of words using split()'''
    words = len(story.split())
    stats["words"] = words


def get_sentences(story):
    '''Count number of sentences by counting terminal punctuation(?,!,.)'''
    # is this really true?
    # "this is Mr. Smith's Cat.  Hello!"
    x = story.count('.')
    y = story.count('?')
    z = story.count('!')
    sentences = x + y + z
    stats["sentences"] = sentences


def get_paragraphs(story):
    '''Count number of paragraphs by splitting on 2 newlines.'''
    paragraphs = story.split("\n\n")
    number_of_paragraphs = len(paragraphs)
    stats["paragraphs"] = number_of_paragraphs


def get_unique_count(story):
    '''Grab number of unique words.'''
    words = set()
    for word in story.split():
        words.add(word)
    stats["unique"] = len(words)


if __name__ == "__main__":
    main()
