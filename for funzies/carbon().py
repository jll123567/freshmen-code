# hydrocarborn bond generator
#by jill
#im lazy so transistor...there
carbons=""
def main():
    global carbons
    carbons=input('how many carbons are there?(type water() for water)')
    if carbons == "water()":
        def water():
            print('H-O-H')
        water()
        main()
    else:
        def builder():
            global carbons
            

            carbons = int(carbons)
            print ('  H')
            print('  |')
            for i in range(carbons):
                print('H-C-H')

            print('  |')
            print ('  H')
            h=carbons*2+2
            print('there are',carbons,"carbons and",h,"""hydrogens""")
            if carbons == 8:
                print('vroom vroom, octane baby')
                
            else:
                e=201811419
        builder()
        main()
def life():
    print('you tell me buddy')
def t():
    print('refrences')
main()
