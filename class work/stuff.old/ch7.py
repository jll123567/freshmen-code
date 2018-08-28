def insult_generator(word,name):
    
    print('''you '''+word+' '+name)
def one(list_of_numbers):
    cnt=0
    for n in list_of_numbers:
        print(n)
        n=n%2
        if n !=0:
            cnt=cnt+1
    print('''there are''',cnt,'''odd numbers''')
one([1,2,3,4,5,13,10])
    
def two(list_of_numbers):
    cnt=0
    for n in list_of_numbers:
        print(n)
        n=n%2
        if n ==0:
            cnt=cnt+1
    print('''there are''',cnt,'''even numbers''')
two([1,2,3,4,5,13,10])
def three(list_of_num):
    negadd=0
    do_nothing=''
    for n in list_of_num:
        print(n)
        if n <0:
            negadd=negadd+n
    print('the sum of all the negtive numbers is''',negadd)
three([1,-2,3,-4,-10])
def four(list_of_wrds):
    cnt=0
    for wrd in list_of_wrds:
        print(wrd)
        n=len(wrd)
        if n == 5:
            cnt=cnt+1
    print('''there are/is''',cnt,'''word(s) with legnth 5''')
four(['hey','you','come','across','as','insulting','sometimes','joe','apple'])
def five(list_of_num):
    firsteven=False
    numsum=0
    for n in list_of_num:
        print(n)
        if firsteven==False:
            if n%2 ==0:
                firsteven=True
                print(n,'''it the first even''')
            else:
                numsum=numsum+n
        else:
            numsum=numsum+n
    print(numsum)
five([1,2,3,4,5,6])
def six(list_of_words):
    sam=False
    wrd=0
    for w in list_of_words:
        
        if w =='SAM'or'sam'or'Sam':
            wrd=wrd+1
            sam=True
        else:
            wrd=wrd+1
            nosam=nosam+1
    #if sam:
        #break
            
    print('''there are''',wrd,'''words''')
six(['i','know','sam','the','man'])
            
