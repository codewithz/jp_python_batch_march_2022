import re

word_list = ['haaaa','ha', 'hahahahaha', 'hahaha', 'hahahaha', 'haha',
             'hahahahahaha', 'hahahahahahahaha', 'hahahahahahahahaha']
pattern='(ha){4}'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES for {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")