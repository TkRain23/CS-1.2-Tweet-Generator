import sys
import time
import operator
from collections import Counter


def dictionary_histogram(story):
    """
    Use dictinoaries to take in a source of text to return a histogram.

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
        print(("     {:<10s} \t appearing {} times").format(key, value))

    bottom_5_words = (Counter(recurrence).most_common()[:-6:-1])
    print("\nThe Five Least Common Words Are:\n")
    for key, value in bottom_5_words:
        print(("     {:<10s} \t appearing {} times").format(key, value))

    return recurrence

def count_histogram(story):
    """
    Use counts to take in a source of text to return a histogram.

    The histogram data structure stores each unique word along
    with the number of times the word appears in the source text
    """

    histogram = []

    words = story.split()

    for i in range(len(words)):
        if not len(histogram):
            histogram.append((1, [words[i]]))
        else:
            count = 0
            word_found = False
            word_appended = False
            current_word = words[i]

            for tuple in histogram:
                frequency = tuple[0]
                words_in_tuple = tuple[1]
                if count == frequency:
                    words_in_tuple.append(current_word)
                    word_appended = True
                    break
                if current_word in words_in_tuple:
                    count = frequency + 1
                    word_found = True
                    words_in_tuple.remove(current_word)
                    if not len(words_in_tuple):
                        histogram.remove(tuple)
            if not word_found:
                histogram[0][1].append(current_word)
            elif word_found and not word_appended:
                histogram.append((count, [current_word]))

    # for i in range(len(words)):
    #     if not len(histogram[i][1]):
    #         for tuple in histogram:
    #         histogram.remove(histogram[i])

    histogram.sort(key=lambda tuple:tuple[0])
    return histogram

    # count = Counter()dasf
    # for word in story:
    #     count[word] += 1
    #
    # print(count)
    #
    # top_5_words = (Counter(count).most_common(5))
    # print("\nThe Five Most Common Words Are:\n")
    # for key, value in top_5_words:
    #     print(("     {:<10s} \t appearing {} times").format(key, value))
    #
    # bottom_5_words = (Counter(count).most_common()[:-6:-1])
    # print("\nThe Five Least Common Words Are:\n")
    # for key, value in bottom_5_words:
    #     print(("     {:<10s} \t appearing {} times").format(key, value))
    #
    # return count


def list_histogram(story):
    """
    Use a list of lists to take in a source of text to return a histogram.

    The histogram data structure stores each unique word along
    with the number of times the word appears in the source text
    """
    list_of_words = []

    for word in story:
        if word not in list_of_words:
            list_of_words.append([word, 1])
        for item in list_of_words:
            if item[0] == word:
                item[1] += 1

    print(sorted(list_of_words, key=operator.itemgetter(1)))
    print(sorted(list_of_words, key=operator.itemgetter(1), reverse=True))

    return list_of_words


def tuples_histogram(story):
    """
    Use tuples to take in a source of text to return a histogram.

    The histogram data structure stores each unique word along
    with the number of times the word appears in the source text
    """
    list_of_words = []

    for word in story:
        if word not in list_of_words:
            list_of_words.append((word, story.count(word)))

    print(list_of_words)

    print(sorted(list_of_words, key=operator.itemgetter(1)))
    print(sorted(list_of_words, key=operator.itemgetter(1), reverse=True))

    return list_of_words


def unique_words(recurrence):
    """Take in a histogram to return the total count of unique words."""
    unique_word_count = ("There are {} unique words from this text source.").format(len(recurrence))
    print(("\n{}\n").format(unique_word_count))


def frequency(word, recurrence):
    """Take in a word and histogram to return the frequency of the word."""
    print(("The word '{}' appears {} times.").format(word, recurrence.get(word)))


story = open('basic_text.txt', 'r').read()
print(count_histogram(story))

# if __name__ == '__main__':
#     start_time = time.time()
#     story = open('dracula.txt', 'r').read()
#     word = sys.argv[1]
#     recurrence = dictionary_histogram(story)
#     unique_words(recurrence)
#     frequency(word, recurrence)
#     print(("\nExecuted in: {0:.2f} seconds").format(time.time() - start_time))
