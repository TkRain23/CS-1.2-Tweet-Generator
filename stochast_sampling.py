import random


def unweighted_random(histogram):
    """
    """

    my_words = list(histogram.keys())
    return random.choice(my_words)


def weighted_random(histogram):
    """
    """
    word_count_total = sum(histogram.values())
    current_count = 0
    destination_count = random.randint(0, word_count_total)

    for word, frequency in histogram.items():
        if current_count >= destination_count:
            return word
        else:
            current_count += frequency


def proof(histogram):
    """
    """

    unweighted_results = {}
    for i in range(0, 1000):
        word = unweighted_random(histogram)

        if word in unweighted_results:
            unweighted_results[word] += 1
        else:
            unweighted_results[word] = 1

    weighted_results = {}
    for i in range(0, 1000):
        word = weighted_random(histogram)

        if word in weighted_results:
            weighted_results[word] += 1
        else:
            weighted_results[word] = 1

    print()
    print("---unweighted results---")
    for word, ocurrences in unweighted_results.items():
        print("{} was found: {} times".format(word, ocurrences))

    print()
    print("---weighted results---")
    for word, ocurrences in weighted_results.items():
        print("{} was found: {} times".format(word, ocurrences))


if __name__ == '__main__':
    histogram = {'god': 1, 'fucking': 1, 'kill': 4, 'me': 1, 'please': 2, 'right': 4, 'now': 1, 'yolo': 1}
    proof(histogram)
