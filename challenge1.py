#!/usr/bin/python

file = open("story.txt", "r+")

words = 0
unique = 0
paragraphs = 0
sentences = 0

for word in file.read().split():
    words += 1
    print words
