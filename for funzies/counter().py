# COUNTERS APP
a=0
def main():
    name=input('name it')
    def counter():
        global a
        e=input('press a button to add to the counter(q to quit)')
        if e != "q":
            a = a+1
            print(a)
            counter()
        else:
            main()
    counter()
main()
