# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:53:27 2026

@author: dbara
"""
import string

# a. Open the file for reading. Assume your code and the file are in the same folder.
fileName = 'gettysburg.txt'
with open(fileName, 'r') as file:
    content = file.read()  # Reads the entire file into a string

print(content)

# b. Using the split() and extend() methods define a function speech_to_list() that takes the
# contents of the file and outputs a list containing all the words in the file. Store this in a list called
# speech_list.

def speechToList(fileContent):
    speechList = []  # Initialize an empty list
    for line in fileContent.splitlines():  # Split content into lines
        words = line.split()  # Split each line into words
        speechList.extend(words)  # Add words to the list
    return speechList


speechList = speechToList(content)
print(speechList)  


# c. What is the length of speech_list?

length = len(speechList)
print(f'Length of speechList: {length}')

# d. However, speech_list now contains non-words such as ‘--’. Create another function called
# speech_to_list_better() that uses the append() method to create a list by examining words
# one by one and appending them to the output list only if they aren’t ‘--’. Store this in a list called
# speech_list_better and report its length.

def speechToListBetter(speechList):
    speechListBetter = []  # Initialize an empty list
    for word in speechList:
        if word != '--':  # Exclude unwanted non-words
            speechListBetter.append(word)  # Append valid words
    return speechListBetter


speechListBetter = speechToListBetter(speechList)
newLength = len(speechListBetter)

# print(speechListBetter)
print(f'Length of speechListBetter: {newLength}')

# e. Create a function called unique_words() that takes speech_list_better and outputs a list
# containing only the unique words in Lincoln’s speech. Store this in a list called
# speech_list_unique and report its length. Note here that (i) Capitalization doesn’t affect
# uniqueness, i.e., “we” and “We” are the same word (“we”), and (ii) Surrounding punctuation doesn’t
# affect uniqueness, i.e., “here,” “here.” “Here” and “here” are all the same word (“here”).

def uniqueWords(speechListBetter):
    seen = set()
    speechListUnique = []
    for word in speechListBetter:
        # Convert to lowercase and strip surrounding punctuation
        cleanWord = word.lower().strip(string.punctuation)
        if cleanWord and cleanWord not in seen:
            seen.add(cleanWord)
            speechListUnique.append(cleanWord)
    return speechListUnique

# Example usage
speechListUnique = uniqueWords(speechListBetter)
uniqueLength = len(speechListUnique)

# print(speechListUnique)
print(f'Length of unique words: {uniqueLength}')