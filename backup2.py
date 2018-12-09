sentence_list = []  # create a list that will contain all the words of your sentence
sentence_length = sentence_length + self.order
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
        key = keys[random.randint(0, len(keys))]  # randomly printing none, but why
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
print(sentence_list)
