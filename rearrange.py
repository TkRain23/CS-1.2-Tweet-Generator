import random
import sys

my_words = sys.argv[1:]

rearranged_list = []
rearranged_list = (random.sample(my_words, len(my_words)))

print(*rearranged_list, sep=' ')
