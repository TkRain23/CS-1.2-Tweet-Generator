file = open('stan-transcript-s10-s20.txt', 'w')

with open('southpark-transcript-s10-s20.txt', 'r') as original:
    for line in original:
        if line.strip('\n') in ("Stan"):
            file.write((next(original)))

file.close()
