import random
#when called staes name 7 times
def one():
    for i in range(7):
        print('jacob')
#when called make a tree of *(did you want me to use a loop)
def two():
    print('  *')
    print(' ***')
    print('*****')
    print('  *')
    print('  *')
    print ('marry cristmas')
#finds a cricle's area
def three():
    d=input('diamiter?')
    dd=float(d)
    r=dd/2
    area= 3.14159 * r**2
    print(area)
#temp converter
def four():
    n=input('input a number')
    d=input('convert to (F)arenhight or (C)elsies')
    #checks and convers statement
    if d == 'f':
        c=float(n)
        f=c*1.8
        print(f)
    else:
        f=float(n)
        c=f/1.8
        print(c)
quest=0
dif=0
# a mmath quiz
def five():
   global quest,dif
   prod = 0
   diff=""
   quest=0
#diffucalty
   diff=input('Will it be (h)ard (m)edium or (e)asy')
   if diff == "e":
            dif=10
   if diff == "m":
            dif=25

   if diff == "h":
            dif=100
#ammout of questions
   quest=input("How many questions are there?")
   quest=int(quest)
   if quest <= 10:
       fail()
       print('please do 10 or more questions')
   if quest >= 9:
       cont()
#question generator
def cont():
    global quest,dif
    crt1=2/3
    correct = 0
    crt2=1/3
    for i in range(quest):
        prod = 0
        n1 = random.randint(1, dif)
        n2 = random.randint(1, dif)
        prod = n1 * n2
        ans = 0
        print ('whats' ,n1, "times" ,n2, '''?''')
#awnsering machene
        ans = input("type awnser here")
        ans=int(ans)
        a=float(ans)
        if a == prod:
            print ("That's right -- well done.")
            correct = correct + 1
        else:
            print ("No, I'm afraid the answer is" ,prod)
#Grade
    print("you got" ,correct, 'out of',quest)
    crt0=float(correct)
    if crt0 > crt1:
        print ('good job!')
    if crt0 < crt1 and crt0 > crt2:
        print('you need a little more practice')
    if crt0 < crt2:
        print('you need help')
    if crt0==0:
        fail()
        
#failure of the test  
def fail():
    print('you failed type five() to try again')
