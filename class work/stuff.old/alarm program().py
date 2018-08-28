
import time
x=0.0
n=""
def main():
    global x,n
    x=input('time until event in seconds')
    n=input('name of event')
    print('your event will tigger in', x, "seconds")
    xx=float(x)
    time.sleep(xx)
    nn=str(n)
    print('!!!',nn,"!!!")

main()
#!!!complete!!!
