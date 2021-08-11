def soma( a, b ):
    if len(a) < 8:
        while(len(a)<8):    
            h = '0'
            a = h + a
    if(len(b) < 8):
        while(len(b)<8):    
            h = '0'
            b = h + b
    a = a.split(",")
    b = b.split(",")
    c = []
    i = 0
    carryBit = 0
    while(i <= 9):
        if( a[i] == '0' and b[i] == '0' ):
            if(carryBit == 1):
                c.append(1)
                carryBit = 0
            else:
                c.append(0)
        elif (a[i] == '0' and b[i] == '1'):
            if(carryBit == 1):
                c.append(0)
                carryBit = 1
            else:
                c.append(1)
        elif (a[i] == '1' and b[i] == '0'):  
            if(carryBit == 1):
                c.append(0)
                carryBit = 1
            else:
                c.append(1)
        elif (a[i] == '1' and b[i] == '1'):  
            if(carryBit == 1):
                c.append(1)
                carryBit = 1
            else:
                c.append(0)
                carryBit = 1
    c = c.reverse()
    print('Carry: {}, resultado: {}' .format(carryBit, c))
soma('00011011', '10010110')