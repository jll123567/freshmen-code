

#random module
import random
#text adventutre test
#presets
hp=100
mhp=200
mp=100
ms=""
ps=""
healthpack=10
magickpacs=10
            
#what? don't hate!
def transistor():
    print('------------------------------------------')
    print('you found me!')
    print('             |-----------\   ')
    print("C|-|---------|-O-----o  -| ")
    print("             |-----------/")
    print('------------------------------------------')
#the fight
def fight():
        global hp,mhp,mp,ms,ps
        #status
        print('------------------------------------------')
        print('monster health',mhp)
        print("health",hp,"mana",mp)
        if ms != "":
            global hp,mhp,mp,ms,ps
            print('monster is' ,ms)
        elif ps == "":
            print('you are fine')
        else:
            return

        print('what will you do?')
        print('------------------------------------------')
        #player action
        action=""
        action=input('(a)ttack,(m)agic,(i)tems,(r)un.')
        if action == "a":
            #a basic attack
            global hp,mp,mhp,ms,ps
            atk=0
            atk=random.randint(15,60)
            mhp=mhp-atk
        elif action =="m":
            #magic because magic
            global hp,mp,mhp,ms,ps
            print('(f)ire=20mp')
            print('(i)ce=20mp')
            magicchoise=""
            magicchoise=input('what spell will you use?')
            if magicchoise == "f":
                #fire
                global mp
                statfire=0
                statfire=random.randint(1,100)
                mp=mp-20
                if statfire > 50:
                    global ms,mhp
                    ms="on fire"
                    mhp=mhp-40
            elif magicchoise == "i":
                #ice
                global mp
                statice=0
                statice=random.randint(1,100)
                mp=mp-40
                if statice > 50:
                    global ms,mhp
                    ms="frozen"
                    mhp=mhp-20
        elif action=="i":
            #items
            global mp,hp,mhp,ms,ps,healthpack,magickpacs
            print('(h)ealth packs-50hp-you have',healthpack)
            print('(m)agic packs-20mp-you have',magickpacs)
            itemchoise=""
            itemchoise=input('what will you use?')
            if itemchoise=="h":
                #restore health
                global hp,healthpack
                healthpack=healthpack-1
                hp=hp+50
            elif itemchoise=="m":
                #restore mana
                global mp,magickpacs
                magickpacs=magickpacs-1
                mp=mp+60
        elif action=="r":
            #nice try...
            print('------------------------------------------')
            print("you can't run")
        hit()

def hit():
    #what kind of monster doent hit back?
    global hp
    matk=0
    matk=random.randint(1,25)
    hp=hp-matk
    print('------------------------------------------')
    print('you took', matk,"damage")
    evaluate()
def evaluate():
    #this checks to see if either of you have died yet.
    global hp,mhp,mp,ms,ps
    if mhp <= 0:
        #the end
        money=random.randint(10,30)
        exp=random.randint(30,50)
        print('------------------------------------------')
        print('monster is defeated')
        print('you got',exp,"EXP")
        print('you got',money,"cash")
        print('------------------------------------------')
    elif hp <= 0:
        #try and try again
        print('you lost')
        retry=input('restart?(y/n)')
        if retry == "y":
            hp=100
            mhp=200
            mp=100
            ms=""
            ps=""
            fight()
        else:
            print('ok,good bye!')
    else:
        fight()

def main():
    #the begining
    global qusetstart
    qusetstart=input('Begin? (Y/N)')
    if qusetstart == 'y':
        fight()
main()
#!!!complete!!!(trans ref not done yet)
