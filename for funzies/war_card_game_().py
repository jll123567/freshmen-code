import random
#pvc vars
p=0
pd=21
com=0
comd=21
p1=0
p1d=21
p2=0
p2d=21
def war():
     global p,pd,com,comd,p1,p1d,p2,p2d
     print('Welcome to war!')
     print('')
     ch1=input('how many players((1) or (2))')
     print('')
     if ch1=='1':
          p=0
          pd=21
          com=0
          comd=21
          def pvc():
               global p,pd,com,comd
               go=input('press enter,q to quit')
               print('')
               if go != 'q':
                    if comd == 0:
                         print('player wins')
                         print('')
                         war()
                    elif pd == 0:
                         print('compuer wins')
                         print('')
                         war()
                    else:
                         
                         p=random.randint(1,13)
                         com=random.randint(1,13)
                         if p > com:
                              print('player was higher')
                              print('player has',pd,"cards left")
                              print('')
                              comd=comd-1
                              pd=pd+1
                         elif com > p:
                              print('computer was higher')
                              print('player has',pd,"cards left")
                              print('')
                              pd=pd-1
                              comd=comd+1
                         else:
                              print('tie')
                              print('')
               else:
                    war()
               pvc()
          pvc()
     if ch1=='2':
          p=0
          pd=21
          com=0
          comd=21
          def pvp():
               global p1,p1d,p2,p2d
               go=input('press enter,q to quit')
               print('')
               if go != 'q':
                    if p2d == 0:
                         print('player1 wins')
                         print('')
                         war()
                    elif p1d == 0:
                         print('player2 wins')
                         print('')
                         war()
                    else:
                         
                         p1=random.randint(1,13)
                         p2=random.randint(1,13)
                         if p1 > p2:
                              print('player1 was higher')
                              print('player2 has',p2d,"cards left")
                              print('')
                              p2d=p2d-1
                              p1d=p1d+1
                         elif p2 > p1:
                              print('player2 was higher')
                              print('player1 has',p1d,"cards left")
                              print('')
                              p1d=p1d-1
                              p2d=p2d+1
                         else:
                              print('tie')
                              print('')
               else:
                    war()
               pvp()
          pvp()
     elif ch1 == 't':
          print('transistor')
          print('')
          war()
     else:
          war()
war()
