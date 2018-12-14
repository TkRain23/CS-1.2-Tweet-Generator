
corpus = open('corpus.txt').read()
corpus = corpus.strip().replace('\n', ' ')
new_corpus = open('newcorpus.txt', 'w')
new_corpus.write(corpus)
