
import time
import random
import sys
d=0
chp=0
lc=False
rg=False
sword=False
lg=False
#game funct()n
def game():
    #death function
    def death():
        global d,chp
        if d==True:
            print('game over')
            retry=input('will you try again(y/n)')
            if retry == 'n':
                d=False
                game()
            else:
                if chp == 1:
                    fl2()
                    d=False
                elif chp == 2:
                    fl3()
                    d=False
                elif chp == 3:
                    fl4()
                    d=False
                elif chp == 4:
                    trump()
                    d=False
                else:
                    game()
                    d=False
    print('''you find your self in the middle of a street,
the apocalypse has finally ended,
all you remember are the bombs going off,
the street is long, almost infinite.''')
    time.sleep(5)
    #first option
    def street():
        print('will you continue down the street?')
        ch1=input('(y,n)')
        if ch1 == 'y':
            street()
        elif ch1 =='n':
            print('''
you seek shelter in a nearby building,it is rundown and ramshackle.
little did you know that the building was teeming with monsters''')
        else:
            street()
    street()
    #first floor encounters
    def f1():
        global d,lg,sword
        print('''
you see two weapons as you enter the building, a sword, and a radioactve lazer pistol,
you can only carry one...''')
        ch2=input('(S)word or (L)azer gun?')
        if ch2 == 's':
            print('you take the sword and hope for the best')
            sword = True
            LG=False
        elif ch2 == 'l':
            print('you pick up the gun,it glows a soft yellow')
            LG=True
            sword = False
        else:
            print('you leave them both behind, why? I know not')
        print('''
you walk forward and look for some stairs height and exercise will surely help you...then...
a monster attacks... it looks like a stoner, a rat and baby''')
        ch3=input('fight(y/n)')
        if ch3 == 'y':
            print('''
                     ++++++++++++++++++++++++
                     get a 3 or higher to win
                     ++++++++++++++++++++++++
                 ''')
            atk=random.randint(1,20)
            print('you roll a',atk)
            if atk < 3:
                d=True
                death()
            else:
                print('''
monster slumps in defeat, you also find the stairwell and go on to the next floor''')
        else:
            print('''
the baby stoner rat kills you''')
            d=1
            death()
    f1()
    #check point
    def str1():
        global chp
        print('''
you head up the stairs and find a chckpoint''')
        chp=1
    str1()
    def fl2():
        global d,lc
        print('''
you walk in and see a box,
it's ratlling and whimpering...
suddenly,a mutated version of your good friend, Mr.Moyal appears and may attack
 however, you want to open/shoot the box...''')
        ch4 = input('(S)hoot box or (M)oyal')
        if ch4 == 's':
            print('''
inside was a lazer corgi...
she shoots Moyal and acompanys you''')
            
        else:
            print('''
you shoot moyal but, not before he throws the box out the window.
never to be seen again''')
            print('''
++++++++++++++
roll a 3 of 20
++++++++++++++''')
            atk = random.randint(1,20)
            if atk < 3:
                d=True
                death()
            else:
                print ('''
you defeated  moyal''')
        
    fl2()
    def str2():
        global chp
        print('''
checkpoint!''')
        chp=2
    str2()
    #ya
    def fl3():
        global d
        print('''
you enter a strangely calm room and see a plant.

It fills you with determination(all 100 of 100 hp restored)

you see some sticky notes...''')
        ch5 = input('read sticky notes?(y/n)')
        if ch5=='y':
            print('''
it says "how much does a fat undead warior weigh?
...
A SKELE-TON...
its not that funny...''')
        else:
            print('''
you decide not to read it,
it's probably very corny...''')
        print('''
you see a sign that says...
"stairs are right im left"
its signed -flowey the mutated plant-

you see two doors...''')
        ch6 = input('''
go (l)eft or (r)ight''')
        if ch6 == 'l':
            print('''you head upstairs
good job''')
            chp=3
        else:
            print('''
flowey kills you...
dont listen to mutant writing plants''')
            d=True
            death()
    fl3()
    def fl4():
        global lc,d,rg
        if lc == True:
            print('''
lazer corgi warns you of monster''')
        else:
            print('''
a monster appears''')
        print('''
its camron the jerk,he is sleeping''')
        ch7 = input('fight(y/n)')
        if ch7 == 'y':
            print('''
you wake him up and he kills you''')
            d=True
            death()
        else:
            ch8 = input('steal from him?(y/n)')
            if ch8== 'y':
                print('''you got a railgun''')
                rg=True
            else:
                rg=False
            print('''you move forward''')
    fl4()
    def str3():
        global chp
        print('checkpoint!')
        chp=4
    str3()
    print('''final floor, finaly you will be able to survive''')
    def trump():
        global d,rg,lc,cowardend
        print('''you see a sheild...''')
        if rg==False or lc == True:
            ch9 = input('pick it up?(y/n)')
            if ch9 == 'y':
                sh=True
            elif ch9 == 'n':
                print('''ok?!?!??!?!?''')
                sh=False
        else:
            print('''you have too much stuff''')
            sh=False
        print('''you see something horrific...
its donald trump

"youll never get past me!"
''')
        ch10=input('fight(y/n)')
        if ch10 == 'y':
            print('''prepare yourself
random dice rolls don't work here!!!''')
            ff=True
        else:
            print('''you leave...''')
            cowardend = True
            ff=False
        if ff ==True:
            print('Trump aims left')
            f1=input('l/r')
            if f1 == 'l':
                print('''you are squashed''')
                d=True
                death()
            elif f1=='r':
                print('''you dodge
you chop off one of his four arms
if you can get the rest of them you can get his head
''')
            else:
                print('''he kills you''')
                d=True
                death()
            print('''he plans to shoot you''')
            if sh==True:
                print('''you block his shot''')
            else:
                print('''you dodge his shot''')
            print('''you get a hit in''')
            print('''two to go!''')
            print('''
he aims left(where you are!)
''')
            f2=input('l/r')
            if f2=='l':
                print('''he kills you''')
                d=True
                death()
            else:
                print('''he missed!
you got him
one to go!
''')
            if rg==True:
                print('''you get another shot in and kill him
''')
            elif lc==True:
                print('''your lazer corgi gets a shot in''')
            else:
                rg=False
                lc=False
            if lc == True:
                    print('''you get his head...
now he is dead''')
    trump()
    def ending():
            global cowardend,sword,rg,lg,lc
            if cowardend ==True:
                print('''
you suck, fight like a man''')
            if sword==True:
                print('''
you and your sword defeated the monster''')
            if rg == True:
                print('''
you and your railgun defeated the monster''')
            elif lg == True:
                print('''
you and your lazer gun defeated the monster''')
            if sword==False and lg==False:
                print('''
you beat it with your bare hands''')
            if lc ==True and lg==True:
                print('''
the lazer gun gave you cancer and the lazer corgi heals you...
over a five month period''')
            if lc == True and lg==False:
                print('''
lazer corgi chased a lazer off the roof and died =(''')
            print('you won')
    ending()
game()
