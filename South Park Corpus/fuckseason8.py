file = open('cartman-transcript-s9.txt', 'w')

with open('southpark-transcript-s9.txt', 'r') as original:
    for line in original:
        if line.split('\t')[0] == "Cartman:":
            file.write(line)
file.close()
