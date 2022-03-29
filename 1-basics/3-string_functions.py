name="Zartab"
print(name)
print(type(name));
print(dir(name))
# String can be enclosed in "some string" | 'some string'
#Multi Line String
paragraph="""
India is my country
All Indians are my brother's and sister's
I love my country
"""

print(paragraph)

paragraph='''
India is my country
All Indians are my brother's and sister's
I love my country
'''
print(paragraph)

# some_string="I will meet you at John's"
# some_string='I will meet you at John's'

# Strings are array

word='kitkat'

print(word[1])

print(word[1:3])

print(word[-5])

print(word[0:20])

# print(word[8])
# print(word[8])
# IndexError: string index out of range

# Starts  from 1 from zero based index till the length
print(word[1:])

print(word[:5])


# Length

print("Length",len(word))
# Trimming -- strip()
word_with_spaces="   hello world   ";
print("Length before trimmng",len(word_with_spaces))
print(word_with_spaces)
word_with_spaces=word_with_spaces.strip()
print("Length after trimmng",len(word_with_spaces))
print(word_with_spaces)

#Casing
company='jp morgan'
print("Company:",company)
company=company.upper()
print("Company:",company)

sentence="I AM HAPPY TO BE HERE"
print("Sentence:",sentence)

sentence=sentence.lower()
print("Sentence:",sentence)

sentence=sentence.capitalize();
print("Sentence with Capitalize:",sentence)

sentence=sentence.title()
print("Sentence with Title:",sentence)

#Replacement
language='Jxvx'
print(language)
language=language.replace('x','a')
print(language)

# Split a String

line='1,Tom,IT,Dev,30000'
print("O:",line)

data=line.split(",")
print(data)
print(type(data))

# in keyword

line="My name is Tom"

checkTom="Tom" in line;
print("If Tom keyword is there in line:",checkTom)

checkAlex="Alex" in line;
print("If Alex keyword is there in line:",checkAlex)

# Format function

line="My name is Zartab, I am {} years old"
age=31

fline=line.format(age);
print("O:",line)
print("F:",fline)

line=" My name is {} , I am {} years old"
name="Micheal"
age=35
fline=line.format(name,age)
print("O:",line)
print("F:",fline)

# Numbered Formating

line="Hey I am a {0},I train my {1},{1} asks doubt to {0}"
trainer="Trainer"
trainee="Trainee"

fline=line.format(trainer,trainee)
print("O:",line)
print("F:",fline)

#Named Formatting

line="Hey I am a Trainer, my name is {trainer}, my trainee name is {trainee},{trainee} asks doubt to {trainer}"

fline=line.format(trainee=None,trainer="Tom")
print("O:",line)
print("F:",fline)

# count

name="zartab"

a_count=name.count('a')
print("count of a in ",name,'is',a_count)

#starts with and ends with

print("Starts WIth z",name.startswith('z'))
print("ends WIth B",name.endswith('B'))
print("ends WIth b",name.endswith('b'))
print("ends WIth a",name.endswith('a'))

# Escape Character
#
# \n - New Line
# \t - Tab
# \\ - Backslas
# \" - double quotes

# text='This is a backslash \';
# print(text)

text='This is a backslash \\';
print(text)

text='These are two backslash \\\\';
print(text)

text="I work at \"JP Morgan\""
print(text)
