file = open('cartman-transcript-s10-s20.txt', 'w')

with open('southpark-transcript-s10-s20.txt', 'r') as original:
    for line in original:
        if line.strip('\n') in ("Cartman", "Toddler Cartman"):
            file.write((next(original)))

file.close()
