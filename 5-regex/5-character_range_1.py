import re

word_list =['foo', 'moo', 'coo', 'doo',
            'poo', 'loo', 'boo', 'hoo']  ;

pattern='[fcl]oo'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES for {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")