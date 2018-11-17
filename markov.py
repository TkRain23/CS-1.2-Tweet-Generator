#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
from misc.dictogram import Dictogram

class MarkovChain(dict):
    """TBD"""

    def __init__(self, word_list=None):
        """TBD"""
        super(Dictogram, self).__init__()  # Initialize this as a new dict

    # create a dictionary of histograms
    # first word stored key in the dictionary
    # second word is store as a value which is a histogram
    # keep track of the words when you first see them (current, next)
    # if the word has already been seen and the next word is not unique, proceed
    # else if the word has already been seen


        [red] [blue] fuck you
         i     i+1
        red [blue] [fuck] you
              i     i+1


        my_list = []

        for i in range(len(my_list)):
            current_word = my_list(i)
            next_word = my_list(i+1)
            add
    """
    function that takes in a word list
    """



def main():
    pass


if __name__ == '__main__':
    main()
