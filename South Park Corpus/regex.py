# import re
#
# pattern = r'\[.*?\]'
#
# withbracket = open('withbracket.txt', 'r')
# withoutbracket = open('withoutbracket.txt', 'w')
#
# newshit = re.sub(pattern, '', withbracket)
# withoutbracket.write(newshit)
#
# withbracket.close()
# withoutbracket.close()

import re
pattern = r'\[[^\]]*\] '
pattern2 = r'\[[^\]]*\]'
with open ('cartman-transcript-s1-s20.txt', 'r') as with_bracket:
    content = with_bracket.read()
content_new = re.sub(pattern, '', content)
content_new = re.sub(pattern2, '', content_new)

withoutbracket = open('cartman-transcript-s1-s20-no-brackets.txt', 'w')
withoutbracket.write(content_new)
