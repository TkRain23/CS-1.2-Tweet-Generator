import random
import sys
data = open('words.txt', 'r').read().split()


def random_words():
    word_list = random.sample(data, int(sys.argv[1]))
    print(*word_list, sep=' ', end=""),
    print('.')


random_words()
