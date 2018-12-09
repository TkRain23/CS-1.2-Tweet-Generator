def create_sentence(self, sentence_length=10):
    sentence_list = []

    sentence_length = sentence_length + self.order
    # create a list of keys
    keys = list(self.keys())
    # generate random start point
    start_point_index = random.randint(0, len(keys)) # i put minus self.order? see screenshot
    # generate a starting tuple, based on the random start point
    current_tuple = keys[start_point_index]
    # get the value at the given key
    values = self[current_tuple]

    tuple_as_list = list(current_tuple)

    next_word = weighted_random(values)

    sentence_list = tuple_as_list

    # sentence_list.append(next_word)

    for i in range(0, sentence_length):
        # pick a word from the Dictogram
        while next_word is None:
            key = keys[random.randint(0, len(keys))]  # randomly printing none, but why
            next_word = weighted_random(self[key])
        # [the] -> {boy, dog, potato}
        # [the, dog] -> {ate, killed, raped}, picked ate
        # [dog, ate] ->
        # make a new instance of a tuple to find next value
        sentence_list.append(next_word)
        print("prior removal")
        print(tuple_as_list)
        tuple_as_list = tuple_as_list[1:]
        print("Removed Head from List")
        print(tuple_as_list)

        tuple_as_list.append(next_word)
        print("add new word to tuple")
        print(tuple_as_list)

        new_tuple = tuple(tuple_as_list)
        print("turn tuple into list")
        print(new_tuple)

        next_word = weighted_random(self[new_tuple])

        print('add new word to sentence list')
        print(sentence_list)

        print("=== Printing New List w/ Appended Word ===")
        print(tuple_as_list)

        # don't wrap yet but if wrap
        # wrap = tuple(next_tuple)
        # new_values = self[]

    print("my list")
    print(sentence_list)

    final_sentence = " ".join(sentence_list)
    print(final_sentence)
