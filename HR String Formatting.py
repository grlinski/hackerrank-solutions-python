


def print_formatted(n):
    lb = len(bin(n))-2

    octn = oct(n)
    hexn = hex(n)
    #print(lb)
    #print(octn)
    #print(hexn)

    for i in range(1,n+1):
        # Dec Space
        spacedec = (lb - len(str(i)))
        print(' ' * spacedec, end='')
        print(i,end='')

        # Oct
        octn = str(oct(i))
        octn = octn[2:]

        # Space Oct
        spaceoct = lb-len(octn)+1
        print(' '*spaceoct,end='')
        print(octn,end='')




        # Hex
        hexn = str(hex(i))
        hexn = hexn[2:]
        hexn = hexn.upper()



        # Space Hex
        spaceoct = lb-len(hexn)+1
        print(' '*spaceoct,end='')
        print(hexn,end='')

        # Bin
        binn = str(bin(i))
        binn = binn[2:]

        # Space Bin
        spaceoct = lb-len(binn)+1
        print(' '*spaceoct,end='')
        print(binn)









#n = int(input())
n = 63
print_formatted(n)


