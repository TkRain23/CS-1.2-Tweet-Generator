import random


def random_word(example_list):
    print(random.choice(example_list))


# make a function that will give you the same result as random.choice

    print(ex_list[random.randint(0,len(example_list))])


if __name__ == '__main__':
    # create a list that will be used to output a random word
    ex_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
    # open up a text file
    ex_text = open('basic_text.txt', 'r').read().split()
    random_word(ex_text)
