import random
import sys
from collections import Counter


def histogram(story):
    """
    Take in a source of text to return a histogram.

    The histogram data structure stores each unique word along
    with the number of times the word appears in the source text
    """
    recurrence = {}
    for word in story:
        if(word in recurrence):
            recurrence[word] += 1
        else:
            recurrence[word] = 1

    top_5_words = (Counter(recurrence).most_common(5))
    print("\nThe Five Most Common Words Are:\n")
    for key, value in top_5_words:
        print(("     {} \t appearing {} times").format(key, value))

    bottom_5_words = (Counter(recurrence).most_common()[:-6:-1])
    print("\nThe Five Least Common Words Are:\n")
    for key, value in bottom_5_words:
        print(("     {} \t appearing {} times").format(key, value))

    return recurrence


def unique_words(recurrence):
    """Take in a histogram to return the total count of unique words."""

    unique_word_count = ("There are {} unique words from this text source.").format(len(recurrence))
    print(("\n{}\n").format(unique_word_count))


def frequency(word, recurrence):
    """Take in a word and histogram to return the frequency of the word."""

    print(("The word '{}' appears {} times.").format(word, recurrence.get(word)))


if __name__ == '__main__':
    story = open('basic_text.txt', 'r').read().split()
    word = sys.argv[1]
    recurrence = histogram(story)
    unique_words(recurrence)
    frequency(word, recurrence)
