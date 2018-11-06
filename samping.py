import random


def unweighted_random(histogram):
    my_words = list(histogram.keys())
    return random.choice(my_words)


def weighted_random(histogram):
    my_words = []
    for word, frequency in histogram.items():
        for _ in range(frequency):
            my_words.append(word)
    return random.choice(my_words)


def prove_unweighted(histogram, trials):
    proof_list = {}
    for i in range(trials):
        word = unweighted_random(histogram)
        if word in proof_list:
            proof_list[word] += 1
        else:
            proof_list[word] = 1
    print(proof_list)


def prove_weighted(histogram, trials):
    proof_list = {}
    for i in range(trials):
        word = weighted_random(histogram)
        if word in proof_list:
            proof_list[word] += 1
        else:
            proof_list[word] = 1
    print(proof_list)


if __name__ == '__main__':
    histogram = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}
    trials = 10000
    unweighted_random(histogram)
    weighted_random(histogram)
    prove_unweighted(histogram, trials)
    prove_weighted(histogram, trials)
