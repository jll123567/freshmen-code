#import time just-in-case
import time
#var for time correctly closed
sc=0
#paper boats-"pull me here and push me there"
#^figure out this riddle and you win i guess^
#function to track the sucsessfuls closeings
def sucessful_close_tracker():
    global sc
    print(sc,'times sucessfuly closed')
#second converting functuion
def main():
    #make the seconds input
    s=input('input seconds here>')
    #quit command
    if s=='q':
        global sc
        print('ok,good bye')
        #smiliy man says hello
        print('* U *')
        sc=sc+1
    else:
        #convert s type
        sec=float(s)
        #float because everything uses float
        #use s to create m
        m=sec/60
        #float it
        minute=float(m)
        #use m to make h
        h=sec/3600
        #float it
        hour=float(h)
        #print the time
        print(sec,"seconds is equal to",minute,'munites or',hour,"""hours""")
        #have it wait
        time.sleep(5)
        #restart
        main()
#auto-start
main()
# (its a blank space) = not started
#(=started
#()=finished
#!!!complete!!!=(duh)
#code()
#debuging()
