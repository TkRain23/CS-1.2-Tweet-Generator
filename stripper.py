path = "spongebob.txt"

unsorted_text = open(path, 'r')

unedited_transcripts = unsorted_text.read()

new_path = "spongebob_only.txt"
edited_transcripts = open(new_path, 'w')

for line in unsorted_text:
    if line.split(None, 1)[0] is "Spongebob:":
        edited_transcripts.write(line)
