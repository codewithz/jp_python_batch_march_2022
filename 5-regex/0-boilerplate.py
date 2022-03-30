import re

word_list=['','']

pattern=''

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES for {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")