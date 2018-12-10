from dictogram import Dictogram
from stochast_sampling import weighted_random
import random

# make the markov chain
# dictionary that holds dictionarys

# make a class that extends the built in dictionary


class Markov(dict):

    def __init__(self, word_list=None, order=6):
        super(Markov, self).__init__() # initilizes the dictionary that you're inheriting
        self.empty = True  # if the markov is empty, path hasn't been started
        self.order = order

        if word_list is not None:  # check if the user passed in a owrd list
            self.create_markov(word_list)

    # create the path for the markov to walk throughe
    def create_markov(self, word_list):
        # check the length of the list
        list_length = len(word_list)

        # iterates through the list based on the order
        for i in range(0, list_length-self.order):
            # subtract order to avoid index out of bound
            # stops uncessary iterations
            # i in in list length
            # + 1 variable amounts
            if i +self.order < list_length: # going to be the furthest we're indexing at a given length
            # as long as we are within the list boundaries
                current_type = tuple(word for word in word_list[i:i+self.order])
                    # this statement (current type = key we're sotring in markov)
                    # word for word lis twill grab us all the vlaues from i to i + self.orde rand place in tuple
                next_type = word_list[i +self.order]

                self.add_token(current_type, next_type)

    # inserting key value pairs, where current type is the kye, and next type is value
    def add_token(self, current_type, next_type):
        # check if empty
        if self.empty:
            self.empty = False
            self[current_type] = Dictogram([next_type])
        else:
            #make sure key you're trying to insert is in your markov or not
            if current_type in self:
                self[current_type].add_count(next_type)
            else:
                # we dont have anything to retrieve, therefore create key value pair
                self[current_type] = Dictogram([next_type])

    # generates a sentence
    def create_sentence(self, sentence_length=20):
        sentence_list = []  # create a list that will contain all the words of your sentence
        sentence_length = sentence_length - self.order
        keys = list(self.keys())  # create a list of keys
        start_point_index = random.randint(0, len(keys))  # generate random start point
        print("=== Random Starting Number ===")
        print(start_point_index)
        current_tuple = keys[start_point_index]  # generate a starting tuple, based on the random start point
        print("=== KEY AKA STARTING TUPLE AKA CURRENT ===")
        print(current_tuple)
        dictogram = self[current_tuple] #get the dictogram value of the given key value
        print("=== DICTOGRAM ASSOCIATED WITH INITIAL KEY ===")
        print(dictogram)
        tuple_as_list = list(current_tuple) # turns the original tuple into a list for your sentence
        print("=== KEY BUT IT'S A LIST NOW ===")
        print(tuple_as_list)

        sentence_list = tuple_as_list
        print("=== PRINT YOUR SENTENCE LIST ===")
        print(sentence_list)

        # sentence_list.append(next_word)

        next_word = weighted_random(dictogram)
        print("=== THE NEXT FUCKING WORD ===")
        print(next_word)

        print("=== GET READY FOR THE FUCKING FOR LOOP MOTHA FUCKA ===")

        for i in range(0, sentence_length):
            # pick a word from the Dictogram
            while next_word is None:
                keys = keys[random.randint(0, len(keys))]  # randomly printing none, but why
                next_word = weighted_random(self[key])
            # make a new instance of a tuple to find next value
            print("=== TUPLE AS LIST ===")
            print(tuple_as_list)
            tuple_as_list = tuple_as_list[1:]
            print("=== REMOVE THE HEAD ===")
            print(tuple_as_list)
            tuple_as_list.append(next_word)
            print("=== ADDED NEW WORD ===")
            print(tuple_as_list)
            current_tuple = tuple(tuple_as_list)
            print("=== TURN LIST BACK TO TUPLE ===")
            print(current_tuple)
            dictogram = self[current_tuple]
            print("=== UPDATED DICTOGRAM BASED ON NEW TUPLE ===")
            next_word = weighted_random(dictogram)
            sentence_list.append(next_word)
        final_sentence = " ".join(sentence_list)
        return final_sentence


def main():
    # corpus = open('newcorpus.txt', 'r')
    corpus = open('newcorpus.txt', 'r')
    corpus_list = []
    for line in corpus:
        corpus_list.append(line)
    # print("=== Printing Corpus ===")
    # print(corpus_list[0].split())
    markov = Markov(corpus_list[0].split())
    return markov

main()
