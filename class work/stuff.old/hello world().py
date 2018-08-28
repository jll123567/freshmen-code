#time module
import time
#global var
money = 20
act = 0
items = "wallet"
#hidden reference just cuz
def transistor ():
    global money
    money = money + 100
    print ("congrats, here's 100 dolars")
    print(money)




#function that puts money in an acount 
def bank():
    global money,act,items
    act = money
    money= 0
    items=items+ "bankcard,"
    time.sleep(1)
    print("you have$" ,act, 'in your acount')
    print('use unbank() to get your cash')

#unbank
def unbank():
    global money,act
    money = act
    act = 5
    time.sleep(1)
    print("you have$" ,act, 'in your acount from intrest')
    



#function to by a hammer
#rember to include hammer time joke(done)
def hamer_get():
    global money,items
    money = money - 10
    print('got a hammer!')
    print ('hammer added to items')
    items = items + 'hammer,'
    time.sleep(1)
    print ('build a wall?(type build())')


#build that wall
def build():
    global money,items
    print("JK it's hamma time")
    print("if you get the joke please tell Jacob ledbetter")
    money = money + 20
    items = items + "time,"
    print(money)
    print ('you have',items)

    

#main command

print("Hello, World!")
time.sleep(3)
name=input('what is your name')
print('hi',name)
print("I can do math")
time.sleep(3)
print('1+2=')
time.sleep(2)
print(1+2)
time.sleep(3)
print ('ask me about money, by typeing money')
time.sleep(1)
print('type bank() to bank your cash')
time.sleep(1)
print('buy a hammer for $10 by typeing hammer_get()')
print ('you have $',money)
print ("you have",items, 'in your pocket')

#!!!complete!!!
