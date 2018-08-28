
def trans():
    print('             |-----------\   ')
    print('             |   /--\O  -| ')
    print("C|-|---------|-O-----o  -| hi...")
    print('             |   \--/o  -| ')
    print("             |-----------/")
    print('i need help...')
    print('why did i do this?')

def formula():
    awn=0.0
    opp=input('enter your opperator')
    nn1=input('enter first no.')
    nn2=input('enter second no.')
    n1=float(nn1)
    n2=float(nn2)
    if opp =="+":
        awn=n1+n2
        print(awn)
    elif opp =="*":
        awn=n1*n2
        print(awn)
    elif opp=="/":
        awn=n1/n2
        print(awn)
    elif opp=="-":
        awn=n1-n2
        print(awn)
    elif opp=="q":
        main()
    else:
        functuion_fail()
       
def functuion_fail():

    print('please enter +,-,*,or /')
    print('thank you')
    formula()

def math():
    x=input('what is x')
    y=input('what is y')
    if x or y != "q":
        if x < y:
            print(x,'is less than' ,y)
        else:
            if x > y:
                print(x, "is more than",y)
            else:
                print (x, 'and' ,y ,"are equal")
    else:
        main()

    math()

def main():
    option=input('what do you want to do? 1.compare,2. simple math problem. type the no. to begin')
    option=int(option)
    if option == 1 :
         math()
    if option == 2:
        formula()

main()

