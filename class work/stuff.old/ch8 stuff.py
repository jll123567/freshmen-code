 #8.19.1
print('''
y
n
9
myste
True
True
True
True
False
''')
#8.19.2
prefixes='Qu'
suffixes='ack'
print(prefixes+suffixes)
print('''this is dumb
''')
#8.19.3
def count_letters(wrd,let):
    fruit=wrd
    count=0
    print(wrd,let)
    for char in fruit:
        if char == let:
            count += 1
    print(count,'''
''')
count_letters('manbaby','b')
#8.19.
def find_counter(word,letter):
    print(word,letter)
    fwrd=word.find(letter)+1
    print(word.find(letter))
    for i in range(4):
        fwrd=word.find(letter)+1
        print(word.find(letter,fwrd)
find_counter('manbaby','b')
